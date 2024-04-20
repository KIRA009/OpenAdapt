"""This module contains the functions to run the dashboard web application."""


import os
import pathlib
import subprocess
import webbrowser

from loguru import logger

from openadapt import config
from openadapt.build_utils import is_running_from_executable
from openadapt.extensions.thread import Thread

from .api.index import run_app


def run() -> Thread:
    """Run the dashboard web application."""
    # change to the client directory
    cur_dir = pathlib.Path(__file__).parent

    def run_client() -> subprocess.Popen:
        """The entry point for the thread that runs the dashboard client."""
        if is_running_from_executable():
            webbrowser.open(
                f"http://localhost:{config.DASHBOARD_SERVER_PORT}/recordings"
            )
            run_app()
            return

        return subprocess.Popen(
            ["node", "index.js"],
            cwd=cur_dir,
            env={
                **os.environ,
                "DASHBOARD_CLIENT_PORT": str(config.DASHBOARD_CLIENT_PORT),
                "DASHBOARD_SERVER_PORT": str(config.DASHBOARD_SERVER_PORT),
            },
        )

    return Thread(
        target=run_client,
        daemon=True,
        args=(),
    )


def cleanup(process: subprocess.Popen) -> None:
    """Cleanup the dashboard web application process."""
    logger.debug("Terminating the dashboard client.")
    if process:
        process.terminate()
        process.wait()
    logger.debug("Dashboard client terminated.")

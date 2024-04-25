"""API endpoints for recordings."""

from fastapi import APIRouter

from openadapt.app.cards import is_recording, quick_record, stop_record
from openadapt.db import crud
from openadapt.models import Recording


class RecordingsAPI:
    """API endpoints for recordings."""

    def __init__(self) -> None:
        """Initialize the RecordingsAPI class."""
        self.app = APIRouter()

    def attach_routes(self) -> APIRouter:
        """Attach routes to the FastAPI app."""
        self.app.add_api_route("", self.get_recordings, response_model=None)
        self.app.add_api_route("/start", self.start_recording)
        self.app.add_api_route("/stop", self.stop_recording)
        self.app.add_api_route("/status", self.recording_status)
        self.app.add_api_route("/scrub/{recording_id}", self.scrub_recording)
        return self.app

    @staticmethod
    def get_recordings() -> dict[str, list[Recording]]:
        """Get all recordings."""
        recordings = crud.get_all_recordings()
        return {"recordings": recordings}

    @staticmethod
    def start_recording() -> dict[str, str]:
        """Start a recording session."""
        quick_record()
        return {"message": "Recording started"}

    @staticmethod
    def stop_recording() -> dict[str, str]:
        """Stop a recording session."""
        stop_record()
        return {"message": "Recording stopped"}

    @staticmethod
    def recording_status() -> dict[str, bool]:
        """Get the recording status."""
        return {"recording": is_recording()}

    @staticmethod
    def scrub_recording(recording_id: int) -> dict[str, str]:
        crud.new_session()
        recording = crud.get_recording_by_id(recording_id)
        if recording is None:
            return {"message": "Recording not found"}
        crud.scrub_recording(recording)
        return {"message": "abc"}

"""add WindowEvent.state

Revision ID: 57d78d23087a
Revises: 20f9c2afb42c
Create Date: 2023-05-14 18:32:57.473479

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "57d78d23087a"
down_revision = "20f9c2afb42c"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("window_event", schema=None) as batch_op:
        batch_op.add_column(sa.Column("state", sa.JSON(), nullable=True))

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("window_event", schema=None) as batch_op:
        batch_op.drop_column("state")

    # ### end Alembic commands ###

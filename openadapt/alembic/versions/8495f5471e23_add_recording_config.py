"""add Recording.config

Revision ID: 8495f5471e23
Revises: 30a5ba9d6453
Create Date: 2024-05-02 15:08:30.109181

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "8495f5471e23"
down_revision = "30a5ba9d6453"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("recording", schema=None) as batch_op:
        batch_op.add_column(sa.Column("config", sa.JSON(), nullable=True))

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("recording", schema=None) as batch_op:
        batch_op.drop_column("config")

    # ### end Alembic commands ###

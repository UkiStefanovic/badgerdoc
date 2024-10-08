# type: ignore
"""empty message

Revision ID: 83694c0b2df6
Revises: 7511c6790067
Create Date: 2021-12-01 14:48:13.568404

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "83694c0b2df6"
down_revision = "7511c6790067"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "job",
        sa.Column("validation_type", sa.String(length=30), nullable=True),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("job", "validation_type")
    # ### end Alembic commands ###

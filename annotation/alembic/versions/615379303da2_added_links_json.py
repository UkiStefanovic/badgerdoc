"""Added links json

Revision ID: 615379303da2
Revises: 7cc1ed83c309
Create Date: 2023-01-20 17:40:36.974060

"""

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "615379303da2"
down_revision = "7cc1ed83c309"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "annotated_docs",
        sa.Column(
            "links_json",
            postgresql.JSON(astext_type=sa.Text()),
            server_default="{}",
            nullable=False,
        ),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("annotated_docs", "links_json")
    # ### end Alembic commands ###

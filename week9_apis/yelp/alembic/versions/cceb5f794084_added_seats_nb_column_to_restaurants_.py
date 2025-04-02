"""added seats_nb column to restaurants table

Revision ID: cceb5f794084
Revises: 6543c8418112
Create Date: 2025-04-02 14:01:19.767108

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cceb5f794084'
down_revision: Union[str, None] = '6543c8418112'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('restaurants', sa.Column('seats_nb', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('restaurants', 'seats_nb')
    # ### end Alembic commands ###

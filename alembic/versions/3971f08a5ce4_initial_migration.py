"""Initial Migration

Revision ID: 3971f08a5ce4
Revises: 
Create Date: 2024-11-17 18:03:49.644948

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3971f08a5ce4'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('asset',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('serial_number', sa.String(), nullable=True),
    sa.Column('hours_state', sa.String(), nullable=True),
    sa.Column('is_working', sa.Boolean(), nullable=True),
    sa.Column('is_fixed_asset', sa.Boolean(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('is_barcode_generated', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('sold_at', sa.DateTime(), nullable=True),
    sa.Column('initial_cost', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_asset_id'), 'asset', ['id'], unique=False)
    op.create_table('model',
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('name'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('model')
    op.drop_index(op.f('ix_asset_id'), table_name='asset')
    op.drop_table('asset')
    # ### end Alembic commands ###
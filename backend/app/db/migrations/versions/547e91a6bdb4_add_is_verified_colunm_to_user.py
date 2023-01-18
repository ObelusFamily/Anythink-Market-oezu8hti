"""add is_verified colunm to user

Revision ID: 547e91a6bdb4
Revises: fdf8821871d7
Create Date: 2023-01-18 12:21:23.509253

"""
from alembic import op
import sqlalchemy as sa


revision = '547e91a6bdb4'
down_revision = 'fdf8821871d7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('users', sa.Column('is_verified', sa.Boolean, nullable=True))
    op.execute('update users set is_verified=false')
    op.alter_column('users', 'is_verified', nullable=False)


def downgrade() -> None:
    pass

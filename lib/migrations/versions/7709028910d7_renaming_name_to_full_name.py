"""Renaming name to full_name

Revision ID: 7709028910d7
Revises: 791279dd0760
Create Date: 2025-12-05 11:55:06.069715

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7709028910d7'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Drop the index on 'name'
    op.drop_index('ix_students_name', table_name='students')
    # Rename the column from 'name' to 'full_name'
    op.alter_column('students', 'name', new_column_name='full_name')
    # Create the index on 'full_name'
    op.create_index(op.f('ix_students_full_name'), 'students', ['full_name'], unique=False)


def downgrade() -> None:
    # Drop the index on 'full_name'
    op.drop_index('ix_students_full_name', table_name='students')
    # Rename the column from 'full_name' back to 'name'
    op.alter_column('students', 'full_name', new_column_name='name')
    # Create the index on 'name'
    op.create_index(op.f('ix_students_name'), 'students', ['name'], unique=False)

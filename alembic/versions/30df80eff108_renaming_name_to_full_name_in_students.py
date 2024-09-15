"""Renaming name to full_name in students

Revision ID: 30df80eff108
Revises: 
Create Date: 2024-09-15 13:24:24.416380

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30df80eff108'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('students', 'name', new_column_name='full_name')

def downgrade() -> None:
    op.alter_column('students', 'full_name', new_column_name='name')

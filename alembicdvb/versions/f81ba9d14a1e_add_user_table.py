"""add user table

Revision ID: f81ba9d14a1e
Revises: afccabcb5532
Create Date: 2021-11-30 00:37:45.930217

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import TIMESTAMP

# revision identifiers, used by Alembic.
revision = 'f81ba9d14a1e'
down_revision = 'afccabcb5532'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )

def downgrade():
    op.drop_table('users')

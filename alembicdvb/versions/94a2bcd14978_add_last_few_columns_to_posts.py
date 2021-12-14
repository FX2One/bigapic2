"""add last few columns to posts

Revision ID: 94a2bcd14978
Revises: 6f040d3659e6
Create Date: 2021-11-30 09:34:07.182238

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '94a2bcd14978'
down_revision = '6f040d3659e6'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)

def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')

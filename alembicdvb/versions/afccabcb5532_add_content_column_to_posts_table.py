"""add content column to posts table

Revision ID: afccabcb5532
Revises: 2dcc2e412881
Create Date: 2021-11-30 00:27:11.609425

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'afccabcb5532'
down_revision = '2dcc2e412881'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content',sa.String, nullable=False))


def downgrade():
    op.drop_column('posts','content')

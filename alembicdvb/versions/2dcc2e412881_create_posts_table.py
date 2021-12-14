"""create posts table

Revision ID: 2dcc2e412881
Revises: 
Create Date: 2021-11-29 15:07:32.537446

"""
from alembic import op
import sqlalchemy as sa



# revision identifiers, used by Alembic.
revision = '2dcc2e412881'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'posts',
        sa.Column('id', sa.Integer,primary_key=True, nullable=False),
        sa.Column('title', sa.String,nullable=False)
    )


def downgrade():
    op.drop_table('posts')


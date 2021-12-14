"""add foreign key to post table

Revision ID: 6f040d3659e6
Revises: f81ba9d14a1e
Create Date: 2021-11-30 09:02:06.655201

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6f040d3659e6'
down_revision = 'f81ba9d14a1e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer, nullable=False))
    op.create_foreign_key('posts_users_fk', source_table='posts',referent_table='users',local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')



def downgrade():
    pass

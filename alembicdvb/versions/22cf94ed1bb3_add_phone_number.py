"""add phone number

Revision ID: 22cf94ed1bb3
Revises: 62e5345eb355
Create Date: 2021-11-30 11:32:59.023188

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '22cf94ed1bb3'
down_revision = '62e5345eb355'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('phone_number', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'phone_number')
    # ### end Alembic commands ###

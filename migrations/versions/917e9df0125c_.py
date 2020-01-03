"""empty message

Revision ID: 917e9df0125c
Revises: de17d1f8a432
Create Date: 2020-01-03 18:09:43.265879

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '917e9df0125c'
down_revision = 'de17d1f8a432'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('book', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'book', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'book', type_='foreignkey')
    op.drop_column('book', 'user_id')
    # ### end Alembic commands ###
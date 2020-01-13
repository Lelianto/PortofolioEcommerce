"""empty message

Revision ID: 1f54cffc1814
Revises: a3fcffd8170c
Create Date: 2020-01-12 19:54:34.049641

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f54cffc1814'
down_revision = 'a3fcffd8170c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('book', sa.Column('email_user', sa.String(length=255), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('book', 'email_user')
    # ### end Alembic commands ###
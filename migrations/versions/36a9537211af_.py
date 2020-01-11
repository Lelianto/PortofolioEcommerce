"""empty message

Revision ID: 36a9537211af
Revises: a2ddf20ffeb3
Create Date: 2020-01-04 11:24:26.684854

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '36a9537211af'
down_revision = 'a2ddf20ffeb3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('cart_ibfk_1', 'cart', type_='foreignkey')
    op.drop_column('cart', 'total_beli')
    op.drop_column('cart', 'book_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cart', sa.Column('book_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.add_column('cart', sa.Column('total_beli', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    op.create_foreign_key('cart_ibfk_1', 'cart', 'book', ['book_id'], ['id'])
    # ### end Alembic commands ###
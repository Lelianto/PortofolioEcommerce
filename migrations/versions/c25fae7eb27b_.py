"""empty message

Revision ID: c25fae7eb27b
Revises: ba727a6dfe20
Create Date: 2020-01-04 13:58:55.845091

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c25fae7eb27b'
down_revision = 'ba727a6dfe20'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cart_detail')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cart_detail',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('cart_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('book_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('total_beli', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], name='cart_detail_ibfk_1'),
    sa.ForeignKeyConstraint(['cart_id'], ['cart.id'], name='cart_detail_ibfk_2'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###

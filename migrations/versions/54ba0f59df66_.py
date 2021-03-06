"""empty message

Revision ID: 54ba0f59df66
Revises: 1f54cffc1814
Create Date: 2020-01-12 21:12:03.346308

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '54ba0f59df66'
down_revision = '1f54cffc1814'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cart', sa.Column('status_jual', sa.String(length=255), nullable=False))
    op.alter_column('cart', 'status_cart',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True)
    op.drop_column('cart', 'nama_lengkap')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cart', sa.Column('nama_lengkap', mysql.VARCHAR(length=255), nullable=False))
    op.alter_column('cart', 'status_cart',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=False)
    op.drop_column('cart', 'status_jual')
    # ### end Alembic commands ###

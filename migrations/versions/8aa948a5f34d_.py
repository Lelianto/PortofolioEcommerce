"""empty message

Revision ID: 8aa948a5f34d
Revises: 
Create Date: 2020-01-03 14:38:05.238684

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8aa948a5f34d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('judul', sa.String(length=255), nullable=False),
    sa.Column('penulis', sa.String(length=255), nullable=False),
    sa.Column('jumlah_halaman', sa.Integer(), nullable=False),
    sa.Column('tanggal_terbit', sa.String(length=255), nullable=False),
    sa.Column('isbn', sa.String(length=50), nullable=False),
    sa.Column('genre', sa.String(length=255), nullable=False),
    sa.Column('bahasa', sa.String(length=255), nullable=False),
    sa.Column('berat', sa.Integer(), nullable=False),
    sa.Column('lebar', sa.Integer(), nullable=False),
    sa.Column('panjang', sa.Integer(), nullable=False),
    sa.Column('jenis_cover', sa.String(length=255), nullable=False),
    sa.Column('status', sa.String(length=255), nullable=False),
    sa.Column('foto_buku', sa.String(length=255), nullable=False),
    sa.Column('sinopsis', sa.String(length=10000), nullable=False),
    sa.Column('harga', sa.Integer(), nullable=False),
    sa.Column('stok', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('isbn')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nama_lengkap', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('kata_sandi', sa.String(length=255), nullable=False),
    sa.Column('tanggal_lahir', sa.String(length=10), nullable=True),
    sa.Column('nomor_telepon', sa.String(length=15), nullable=True),
    sa.Column('foto_profil', sa.String(length=500), nullable=True),
    sa.Column('genre', sa.String(length=1000), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('cart',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.Column('total_beli', sa.Integer(), nullable=False),
    sa.Column('total_harga', sa.Integer(), nullable=False),
    sa.Column('status', sa.Boolean(), nullable=False),
    sa.Column('judul', sa.String(length=255), nullable=False),
    sa.Column('penulis', sa.String(length=255), nullable=False),
    sa.Column('jenis_cover', sa.String(length=255), nullable=False),
    sa.Column('foto_buku', sa.String(length=255), nullable=False),
    sa.Column('harga', sa.Integer(), nullable=False),
    sa.Column('stok', sa.Integer(), nullable=False),
    sa.Column('nama_lengkap', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cart')
    op.drop_table('user')
    op.drop_table('book')
    # ### end Alembic commands ###

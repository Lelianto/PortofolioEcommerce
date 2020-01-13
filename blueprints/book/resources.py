import json
from flask import Blueprint
from flask_restful import Resource, Api, reqparse, inputs, marshal
from blueprints import db, app
from sqlalchemy import desc
from .model import Books
from blueprints.user.model import User
from flask_jwt_extended import jwt_required, get_jwt_claims
from blueprints import internal_required

# Membuat blueprint book
bp_book = Blueprint('book', __name__)
api = Api(bp_book)

class BookResource(Resource):
    def __init__(self):
        pass

    def options(self, id=None):
        return {'status':'ok'},200

    # Mengambil semua buku termasuk bukunya sendiri pada sebuah halaman
    @jwt_required
    def get(self):
        claim = get_jwt_claims()

        parser = reqparse.RequestParser()
        parser.add_argument('p', location='json', default=1)
        parser.add_argument('rp', location='json', default=25)
        args = parser.parse_args()

        # Pagination batas hasil pengambilan
        offset = args['rp'] * (args['p'] - 1)

        qry = Books.query

        all_books = []
        for book in qry.limit(args['rp']).offset(offset):
            all_books.append(marshal(book,Books.response_fields))
        return all_books, 200

    # Menambah Buku di dalam database book
    @jwt_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('judul', location='json', help='judul invalid', default ='None', required=True)
        parser.add_argument('penulis', location='json', help='penulis invalid', default = 'None', required=True)
        parser.add_argument('jumlah_halaman', type=int, location='json', help='jumlah halaman invalid', default=0, required=True)
        parser.add_argument('tanggal_terbit', location='json', help='tanggal terbit invalid', default='none', required=True)
        parser.add_argument('isbn', location='json', help='isbn invalid',default='none', required=True)
        parser.add_argument('genre', location='json', help='genre invalid', default=0, required=True)
        parser.add_argument('bahasa', location='json', help='bahasa invalid', default='none', required=True)
        parser.add_argument('berat', type=float, location='json', help='berat invalid',default=0)
        parser.add_argument('lebar', type=float, location='json', help='lebar invalid', default=0)
        parser.add_argument('panjang', type=float, location='json', help='panjang invalid', default=0)
        parser.add_argument('jenis_cover', location='json', help='jenis cover invalid',default='none', required=True)
        parser.add_argument('status', location='json', help='status invalid', default=0, required=True) 
        parser.add_argument('foto_buku', location='json', help='link foto buku invalid',default='none', required=True)
        parser.add_argument('sinopsis', location='json', help='sinopsis invalid', default=0)
        parser.add_argument('harga', type=int, location='json', help='harga invalid',default=0, required=True)
        parser.add_argument('stok', type=int, location='json', help='stok invalid', default=0, required=True)
        parser.add_argument('penerbit', location='json', help='penerbit invalid',default='none', required=True)
        args = parser.parse_args()

        claim = get_jwt_claims()
        #Books = nama kelas di __init__.py
        book = Books(claim['id'], args['judul'],args['penulis'],args['jumlah_halaman'],args['tanggal_terbit'],args['isbn'],args['genre'],args['bahasa'],args['berat'],args['lebar'],args['panjang'],args['jenis_cover'],args['status'],args['foto_buku'],args['sinopsis'],args['harga'],args['stok'], args['penerbit'], claim['email'])
    
        db.session.add(book)
        db.session.commit()

        app.logger.debug('DEBUG : %s', book)

        return marshal(book, Books.response_fields), 200, {'Content-Type':'application/json'}

class BookList(Resource):
    def options(self, id=None):
        return {'status':'ok'},200

    # Mengakses Buku sesuai ID sendiri untuk User, sementara Internal dapat mengakses semua ID - Digunakan untuk update oleh user nantinya
    @jwt_required
    def get(self, id=None):
        qry = Books.query.get(id)
        claim = get_jwt_claims()
        if qry is not None:
            if claim['email'] == 'lian@alterra.id':
                return marshal(qry, User.user_fields), 
            else:
                # Untuk mengakses buku sendiri - Dapat update, dan delete
                if qry and int(claim['id']) == int(qry.user_id):
                    return marshal(qry, Books.response_fields), 200
                # Untuk mengakses bukuorang lain - Hanya dapat membeli
                else:
                    # return {'status': 'NOT FOUND'}
                    return marshal(qry, Books.response_fields), 200
        return {'status': 'NOT FOUND'}, 404

    # Melakukan updating data buku sesuai ID oleh User
    @jwt_required
    def put(self, id=None):
        if id is None:
            return {'message': 'Masukkan ID'}, 400, {'Content-Type':'application/json'}
        elif id is not None:
            parser = reqparse.RequestParser()
            parser.add_argument('judul', location='json', default ='None', required=True)
            parser.add_argument('penulis', location='json', help='penulis invalid', default = 'None', required=True)
            parser.add_argument('jumlah_halaman', type=int, location='json', help='jumlah halaman invalid', default=0, required=True)
            parser.add_argument('tanggal_terbit', location='json', help='tanggal terbit invalid', default='none', required=True)
            parser.add_argument('isbn', location='json', help='isbn invalid',default='none', required=True)
            parser.add_argument('genre', location='json', help='genre invalid', default=0, required=True)
            parser.add_argument('bahasa', location='json', help='bahasa invalid', default='none', required=True)
            parser.add_argument('berat', type=float, location='json', help='berat invalid',default=0, required=True)
            parser.add_argument('lebar', type=int, location='json', help='lebar invalid', default=0)
            parser.add_argument('panjang', type=int, location='json', help='panjang invalid', default=0)
            parser.add_argument('jenis_cover', location='json', help='jenis cover invalid',default='none', required=True)
            parser.add_argument('status', location='json', help='status invalid', default=0, required=True) 
            parser.add_argument('foto_buku', location='json', help='link foto buku invalid',default='none', required=True)
            parser.add_argument('sinopsis', location='json', help='sinopsis invalid', default=0, required=True)
            parser.add_argument('harga', type=int, location='json', help='harga invalid',default=0, required=True)
            parser.add_argument('stok', type=int, location='json', help='stok invalid', default=0, required=True)
            parser.add_argument('penerbit', location='json', help='penerbit invalid', default=0, required=True)
            args = parser.parse_args()

            qry = Books.query.get(id)

            if qry is None:
                return {'penulis':'NOT_FOUND'}, 404
            
            claim = get_jwt_claims()

            qry.user_id = claim['id']
            qry.judul = args['judul']
            qry.penulis = args['penulis']
            qry.jumlah_halaman = args['jumlah_halaman']
            qry.isbn = args['isbn']
            qry.genre = args['genre']
            qry.bahasa = args['bahasa']
            qry.berat = args['berat']
            qry.lebar = args['lebar']
            qry.panjang = args['panjang']
            qry.jenis_cover = args['jenis_cover']
            qry.status = args['status']
            qry.foto_buku = args['foto_buku']
            qry.sinopsis = args['sinopsis']
            qry.harga = args['harga']
            qry.stok = args['stok']
            qry.penerbit = args['penerbit']
            qry.email = args['email']

            db.session.commit()
            return marshal(qry, Books.response_fields), 200, {'Content-Type':'application/json'}
    
    # Menghapus buku sesuai ID
    @jwt_required
    def delete(self, id=None):
        qry = Books.query.get(id)
        if qry is not None:
            # Hard Delete
            claim = get_jwt_claims()
            # Internal dapat menghapus semua buku sesuai ID
            if claim['email'] == 'lian@alterra.id':
                db.session.delete(qry)
                db.session.commit()
                return {'status': 'DELETED'}, 200, {'Content-Type':'application/json'}
            else:
                # User hanya dapat menghapus bukunya sendiri
                if qry and int(claim['id']) == int(qry.user_id):
                    db.session.delete(qry)
                    db.session.commit()
                    return {'status': 'DELETED'}, 200, {'Content-Type':'application/json'}
                return {'status': 'NOT FOUND'}, 404
        return {'status' : 'There are no book with this ID'}, 404, {'Content-Type':'application/json'}

class BookOwn(Resource):
    def options(self, id=None):
        return {'status':'ok'},200
    # Untuk mengambil seluruh buku milik user
    @jwt_required
    def get(self):
        claim = get_jwt_claims()

        parser = reqparse.RequestParser()
        parser.add_argument('p', location='args', default=1)
        parser.add_argument('rp', location='args', default=25)
        args = parser.parse_args()

        # Pagination hasil pengambilan
        offset = args['rp'] * (args['p'] - 1)

        qry = Books.query
        all_books = qry.filter_by(user_id = claim['id']).limit(args['rp']).offset(offset)

        user_book = []
        for book in all_books:
            user_book.append(marshal(book,Books.response_fields))
        return user_book, 200

class BookSearch(Resource):
    def options(self, id=None):
        return {'status':'ok'},200
    # Fitur pencarian sesuai dengan keyword (judul atau penulis)
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('p', location='args', default=1)
        parser.add_argument('rp', location='args', default=25)
        parser.add_argument('keyword', location='args', default='None')
        args = parser.parse_args()

        qry = Books.query
        
        # Search by judul or penulis
        if qry:
            search_result = qry.filter(Books.judul.like('%' + args['keyword'] + '%') | Books.penulis.like('%' + args['keyword'] + '%'))  
            all_search = []
            for result in search_result:
                all_search.append(marshal(result, Books.response_fields))
            return all_search, 200
        return {'status': 'NOT FOUND'}, 404

class BookCategory(Resource):
    def options(self, id=None):
        return {'status':'ok'},200
    # Pencarian Buku sesuai genre
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('p', location='args', default=1)
        parser.add_argument('rp', location='args', default=25)
        parser.add_argument('keyword', location='args', default='None')
        args = parser.parse_args()

        qry = Books.query
        
        # Search by category
        if qry:
            search_result = qry.filter(Books.genre.like('%' + args['keyword'] + '%'))  
            all_search = []
            for result in search_result:
                all_search.append(marshal(result, Books.response_fields))
            return all_search, 200
        return {'status': 'NOT FOUND'}, 404

api.add_resource(BookOwn, '/mine')
api.add_resource(BookCategory, '/category')
api.add_resource(BookSearch, '/search')
api.add_resource(BookResource, '')
api.add_resource(BookList, '/edit/<id>')

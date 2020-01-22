import json
from flask import Blueprint
from flask_restful import Resource, Api, reqparse, inputs, marshal
from blueprints import db, app
from sqlalchemy import desc
from .model import Books
from blueprints.user.model import User
from flask_jwt_extended import jwt_required, get_jwt_claims
from blueprints import internal_required

# Make a book's blueprint
bp_book = Blueprint('book', __name__)
api = Api(bp_book)

class BookResource(Resource):
    """
    'self' is a variable that represents a function in a class so that the function can be reused in the same class.
    """
    def __init__(self):
        pass

    def options(self, id=None):
        """
        To control errors caused by CORS
        """
        return {'status':'ok'},200

    def get(self):
        """
        Method: GET
        Take all the books including the book itself on a page
        ______________
        
        Parameter Input
        _______________

        p: integer (not required),
             p is the index number of the page that the user wants to display.
        rp: integer (not required),
             rp is the number of outputs that will be displayed on one page.
        Books: query of products,
             Books are objects that exist in the book product table.
        """
        claim = get_jwt_claims()

        parser = reqparse.RequestParser()
        parser.add_argument('p',type=int, location='args', default=1)
        parser.add_argument('rp', type=int, location='args', default=25)
        args = parser.parse_args()

        # Pagination: retrieval limit
        offset = args['rp'] * (args['p'] - 1)

        qry = Books.query

        all_books = []
        for book in qry.limit(args['rp']).offset(offset):
            all_books.append(marshal(book,Books.response_fields))
        return all_books, 200, {'Content-Type':'application/json'}

    @jwt_required
    def post(self):
        """
        Method: POST
        Add books in the book database
        ______________
        
        Parameter Input
        _______________

        judul, penulis, tanggal_terbit, isbn, bahasa, genre, jenis_cover, status, foto_buku, sinopsis, penerbit : string, 
             This input will be the data in the book table.
        we can enter user input data into the table using db.commit ().
        """
        parser = reqparse.RequestParser()
        parser.add_argument('judul', location='json', help='judul invalid', default ='None', required=True)
        parser.add_argument('penulis', location='json', help='penulis invalid', default = 'None', required=True)
        parser.add_argument('jumlah_halaman', type=int, location='json', help='jumlah halaman invalid', default=0, required=True)
        parser.add_argument('tanggal_terbit', location='json', help='tanggal terbit invalid', default='none', required=True)
        parser.add_argument('isbn', location='json', help='isbn invalid',default='none', required=True)
        parser.add_argument('genre', location='json', help='genre invalid', default='none', required=True)
        parser.add_argument('bahasa', location='json', help='bahasa invalid', default='none', required=True)
        parser.add_argument('berat', type=float, location='json', help='berat invalid',default=0)
        parser.add_argument('lebar', type=float, location='json', help='lebar invalid', default=0)
        parser.add_argument('panjang', type=float, location='json', help='panjang invalid', default=0)
        parser.add_argument('jenis_cover', location='json', help='jenis cover invalid',default='Soft Cover', required=True)
        parser.add_argument('status', location='json', help='status invalid', default=0, required=True) 
        parser.add_argument('foto_buku', location='json', help='link foto buku invalid',default='none', required=True)
        parser.add_argument('sinopsis', location='json', help='sinopsis invalid', default='')
        parser.add_argument('harga', type=int, location='json', help='harga invalid',default=0, required=True)
        parser.add_argument('stok', type=int, location='json', help='stok invalid', default=0, required=True)
        parser.add_argument('penerbit', location='json', help='penerbit invalid',default='', required=True)
        args = parser.parse_args()

        claim = get_jwt_claims()
        book = Books(claim['id'], args['judul'],args['penulis'],args['jumlah_halaman'],args['tanggal_terbit'],args['isbn'],args['genre'],args['bahasa'],args['berat'],args['lebar'],args['panjang'],args['jenis_cover'],args['status'],args['foto_buku'],args['sinopsis'],args['harga'],args['stok'], args['penerbit'], claim['email'])
    
        db.session.add(book)
        db.session.commit()

        app.logger.debug('DEBUG : %s', book)

        return marshal(book, Books.response_fields), 200, {'Content-Type':'application/json'}

class BookList(Resource):
    """
    'self' is a variable that represents a function in a class so that the function can be reused in the same class.
    """
    def options(self, id=None):
        """
        To control errors caused by CORS
        """
        return {'status':'ok'},200

    @jwt_required
    def get(self, id=None):
        """
        Method: GET
        Accessing the Book according to its own ID for the User, while Internal can access all IDs - Used to update by the user later
        ______________
        
        Parameter Input
        _______________

        id: params (required),
             id entered by the user.
        Books: query of products,
             Books are objects that exist in the book product table.
        """
        qry = Books.query.get(id)
        claim = get_jwt_claims()
        if qry is not None:
            if claim['email'] == 'lian@alterra.id':
                return marshal(qry, Books.response_fields), 
            else:
                """
                To access your own book - Can update, and delete
                """
                if qry and int(claim['id']) == int(qry.user_id):
                    return marshal(qry, Books.response_fields), 200, {'Content-Type':'application/json'}
                """
                To access other people's books - Can only buy
                """
                return marshal(qry, Books.response_fields), 200, {'Content-Type':'application/json'}
        return {'status': 'NOT FOUND'}, 404, {'Content-Type':'application/json'}

    @jwt_required
    def put(self, id=None):
        """
        Method: PUT
        Updating the book data according to ID by the User
        ______________
        
        Parameter Input
        _______________

        id: params (required),
             id entered by the user.
        judul, penulis, tanggal_terbit, isbn, bahasa, genre, jenis_cover,
        status, foto_buku, sinopsis, penerbit : string, 
             This input will be the data in the book table.
        """
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
                return {'penulis':'NOT_FOUND'}, 404, {'Content-Type':'application/json'}
            
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
            qry.email_user = claim['email']

            db.session.commit()
            return marshal(qry, Books.response_fields), 200, {'Content-Type':'application/json'}
    
    @jwt_required
    def delete(self, id=None):
        """
        Method: DELETE
        Deleting the book data according to ID by the User
        ______________
        
        Parameter Input
        _______________

        id: params (required),
             id entered by the user. Using hard delete.
        """
        qry = Books.query.get(id)
        if qry is not None:
            claim = get_jwt_claims()
            if claim['email'] == 'lian@alterra.id':
                """
                The admin can delete all books according to ID
                """
                db.session.delete(qry)
                db.session.commit()
                return {'status': 'DELETED'}, 200, {'Content-Type':'application/json'}
            else:
                if qry and int(claim['id']) == int(qry.user_id):
                    """
                    Users can only delete their own books
                    """
                    db.session.delete(qry)
                    db.session.commit()
                    return {'status': 'DELETED'}, 200, {'Content-Type':'application/json'}
                return {'status': 'NOT FOUND'}, 404
        return {'status' : 'There are no book with this ID'}, 404, {'Content-Type':'application/json'}

class BookOwn(Resource):
    """
    'self' is a variable that represents a function in a class so that the function can be reused in the same class.
    """
    def options(self, id=None):
        """
        To control errors caused by CORS
        """
        return {'status':'ok'},200

    @jwt_required
    def get(self):
        """
        Method: GET
        To retrieve all user's books
        ______________
        
        Parameter Input
        _______________

        p: integer (not required),
             p is the index number of the page that the user wants to display.
        rp: integer (not required),
             rp is the number of outputs that will be displayed on one page.
        Books: query of products,
             Books are objects that exist in the book product table.
        """
        claim = get_jwt_claims()
        parser = reqparse.RequestParser()
        parser.add_argument('p', location='args', default=1)
        parser.add_argument('rp', location='args', default=25)
        args = parser.parse_args()

        # Pagination retrieval results
        offset = args['rp'] * (args['p'] - 1)

        qry = Books.query
        all_books = qry.filter_by(user_id = claim['id']).limit(args['rp']).offset(offset)

        user_book = []
        for book in all_books:
            user_book.append(marshal(book,Books.response_fields))
        return user_book, 200, {'Content-Type':'application/json'}

class BookSearch(Resource):
    """
    'self' is a variable that represents a function in a class so that the function can be reused in the same class.
    """
    def options(self, id=None):
        """
        To control errors caused by CORS
        """
        return {'status':'ok'},200, {'Content-Type':'application/json'}
 
    def get(self):
        """
        Method: GET
        Search features according to keywords (title or author)
        ______________
        
        Parameter Input
        _______________

        p: integer (not required),
            p is the index number of the page that the user wants to display.
        rp: integer (not required),
            rp is the number of outputs that will be displayed on one page.
        Books: query of products,
            Books are objects that exist in the book product table.
        keyword: string (not required),
            A keyword is a group of characters entered by a user
        """
        parser = reqparse.RequestParser()
        parser.add_argument('p', location='args', default=1)
        parser.add_argument('rp', location='args', default=25)
        parser.add_argument('keyword', location='args', default='')
        args = parser.parse_args()

        qry = Books.query
        
        if qry:
            """
            Search by user based on title, author, book selling status, and book genre.
            """
            search_result = qry.filter(Books.judul.like('%' + args['keyword'] + '%') | Books.penulis.like('%' + args['keyword'] + '%') | Books.status.like('%' + args['keyword'] + '%') | Books.genre.like('%' + args['keyword'] + '%'))  
            all_search = []
            for result in search_result:
                all_search.append(marshal(result, Books.response_fields))
            return all_search, 200
        return {'status': 'NOT FOUND'}, 404, {'Content-Type':'application/json'}

class BookCategory(Resource):
    """
    'self' is a variable that represents a function in a class so that the function can be reused in the same class.
    """
    def options(self, id=None):
        """
        To control errors caused by CORS
        """
        return {'status':'ok'},200, {'Content-Type':'application/json'}
   
    def get(self):
        """
        Method: GET
        Book Search by category
        ______________
        
        Parameter Input
        _______________

        p: integer (not required),
            p is the index number of the page that the user wants to display.
        rp: integer (not required),
            rp is the number of outputs that will be displayed on one page.
        Books: query of products,
            Books are objects that exist in the book product table.
        keyword: string (not required),
            A keyword is a group of characters entered by a user
        """
        parser = reqparse.RequestParser()
        parser.add_argument('p', location='args', default=1)
        parser.add_argument('rp', location='args', default=25)
        parser.add_argument('keyword', location='args', default='None')
        args = parser.parse_args()

        qry = Books.query
  
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

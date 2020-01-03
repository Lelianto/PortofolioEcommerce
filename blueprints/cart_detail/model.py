# Import
from blueprints import db
from flask_restful import fields
from blueprints.book.model import Books
from blueprints.cart.model import Cart

# Create Model
class CartDetail(db.Model):
    __tablename__ = 'cart_detail'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'))
    total_beli = db.Column(db.Integer, nullable=False, default=0)
    
    cart_fields = {
        'id': fields.Integer,
        'book_id' : fields.Integer,
        'cart_id' : fields.Integer,
        'total_beli' : fields.Integer
    }

    def __init__(self, book_id, cart_id, total_beli):
        self.book_id = book_id
        self.cart_id = cart_id
        self.total_beli = total_beli

    # def __repr__(self):
    #     return '<Cart %r>' % self.id
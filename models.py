from website import db
from flask_login import UserMixin
from sqlalchemy.sql import func
#UserMixin is a class that allows in login stuffs

class Notes(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.String(700))
    date = db.Column(db.DateTime(timezone = True), default = func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    #these are the blueprints of the user data that will be stored in our database.
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100) , unique = True)
    password1 = db.Column(db.String(150))
    notes = db.relationship('Notes')

# # Define association table for many-to-many relationship between orders and products
# order_product = db.Table('order_product',
#     db.Column('order_id', db.Integer, db.ForeignKey('order.id'), primary_key=True),
#     db.Column('product_id', db.Integer, db.ForeignKey('product.product_id'), primary_key=True)
# )


class   Product(db.Model):
    product_id = db.Column(db.Integer, primary_key = True)
    productname = db.Column(db.String(100) , nullable = False)
    description = db.Column(db.Text, nullable = False)
    price = db.Column(db.Float, nullable = False)
    # Define many-to-many relationship with Order model
    # orders = db.relationship('Order', secondary=order_product, backref=db.backref('ordered_products', lazy='dynamic'))



# class Order(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     products = db.relationship('Product', secondary='order_product', backref='orders_received')
#     quantity = db.Column(db.Integer, nullable=False)
#     total_price = db.Column(db.Float, nullable=False)
#     shipping_address = db.Column(db.String(100), nullable=False)
#     payment_status = db.Column(db.String(20), nullable=False, default='Pending')

    


    
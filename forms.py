from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectMultipleField, DecimalField
from wtforms.validators import DataRequired, Length, ValidationError
from .models import Product

class OrderForm(FlaskForm):
    shipping_address = StringField('Shipping Address', validators=[DataRequired(), Length(min=5, max=100)])
    products = SelectMultipleField('Products', coerce=int, validators=[DataRequired()])
    total_price = DecimalField('Total Price', places=2, validators=[DataRequired()])
    submit = SubmitField('Place Order')

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        # Query products from the database and populate the SelectMultipleField
        self.products.choices = [(product.id, product.name) for product in Product.query.all()]

from flask import Blueprint, render_template, url_for, request
from flask_login import current_user, login_required
from flask import render_template, url_for, redirect
from .forms import OrderForm
from .models import Product

views = Blueprint('views' , __name__)

@views.route('/')
def homepage():
    return render_template("homepage.html")

@views.route('/home')
@login_required
def home():
    products = Product.query.all()
    return render_template("home.html" , new_user = current_user , products = products)

@views.route('/contact' , methods = ['GET' , 'POST'])
def contact():
    return render_template("contact.html" , new_user = current_user)

@views.route("/products" , methods = ['GET', 'POST'])
def products():
    return render_template("products.html" , new_user = current_user)

@views.route('/about' , methods = ['GET' , 'POST'])
def about():
    return render_template("about.html" , new_user = current_user)

@views.route('/place_order', methods=['GET', 'POST'])
def place_order():
    form = OrderForm()
    if form.validate_on_submit():
        # Handle form submission (save order details, calculate total price, etc.)
        return redirect(url_for('order_confirmation'))  # Redirect to order confirmation page after successful submission
    return render_template('place_order.html', form=form)
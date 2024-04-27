from flask import Blueprint, render_template, url_for, redirect, request, app , flash , get_flashed_messages
from flask_login import current_user, login_required
from .models import Product, db

admin = Blueprint('admin' , __name__)

#the following are the admin routes
#/ is the root/main page of the admin interface
@admin.route('/admin')
def producthome():
    return render_template('admin_dashboard.html')

#add_product is where the admin adds the product of choice. for image we fist check the availability
@admin.route('/add_product' , methods = ['POST' , 'GET'])
def add_product():
    if request.method == 'POST':
        name = request.form.get('name')
        description =  request.form.get('description')
        price = request.form.get('price')

        new_product = Product(productname = name , description = description , price = price)
        db.session.add(new_product)
        db.session.commit()
        flash('item added successfully' , category = 'success')
        return redirect(url_for('admin.view_products'))
    

    return render_template('add_product.html')

@admin.route('/edit_products/<int:product_id>/edit', methods=['GET', 'POST'])
def edit_product(product_id):
    product = Product.query.get_or_404(product_id)

    if request.method == 'POST':
        # Update product details
        product.productname = request.form['name']
        product.description = request.form['description']
        product.price = request.form['price']

        db.session.commit()

        flash('Product updated successfully!', 'success')
        return redirect(url_for('admin.view_products'))
    return render_template('edit_product.html', product=product)


@admin.route('/delete_products/<int:product_id>/delete', methods=['POST' , 'GET'])
def delete_products(product_id):
    product = Product.query.get_or_404(product_id)

    # Delete the product from the database
    db.session.delete(product)
    db.session.commit()

    flash('Product deleted successfully!', 'success')
    return redirect(url_for('admin.view_products'))

@admin.route('/confirm_delete/<int:product_id>' , methods = ['POST' , 'GET'] )
def confirm_delete(product_id):
    # Render the confirmation page
    return render_template('confirm_delete.html', product_id=product_id)


@admin.route('/view_products')
def view_products():
    products = Product.query.all()
    return render_template('view_products.html' , products = products)




# @admin.route('/view_orders/<int:product_id>')
# def view_orders(product_id):    
#     products = Product.query.get_or_404(product_id)
#     orders = Order.query.filter_by(product_id = product_id).all()    
#     return render_template('view_orders.html', product=products, orders=orders)  
    

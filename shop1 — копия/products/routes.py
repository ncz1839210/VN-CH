from flask import redirect, render_template, url_for, flash, request, session
from shop1 import db, app
from .models import Brand, Category, Addproduct
from .forms import Addproducts
import secrets


@app.route('/addbrand', methods=['GET', 'POST'])
def addbrand():
    if 'email' not in session:
        flash(f"Please login first", "danger")
        return redirect(url_for('login'))
    if request.method == "POST":
        getbrand = request.form.get('brand')
        brand = Brand(name=getbrand)
        db.session.add(brand)
        flash(f'The brand {getbrand} was added to your database', 'success')
        db.session.commit()
        return redirect(url_for('addbrand'))

    return render_template('products/addbrand.html', brands='brands')


app.route('/addcat', methods=['GET', 'POST'])
def addcat():
    if 'email' not in session:
        flash(f"Please login first", "danger")
        return redirect(url_for('login'))
    if request.method == "POST":
        getbrand = request.form.get('category')
        cat = Category(name=getbrand)
        db.session.add(cat)
        flash(f'The category {getbrand} was added to your database', 'success')
        db.session.commit()
        return redirect(url_for('addbcat'))

    return render_template('products/addbrand.html')


app.route('/addproduct', methods=['GET', 'POST'])
def addproduct():
    brands = Brand.query.all()
    categories = Category.query.all()
    form = Addproducts(request.form)
    return render_template('products/addproduct.html', form=form, title='Add product page', brands=brands, categories=categories)
from flask import Flask, request, render_template, redirect, url_for, flash, send_from_directory
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Product, Category
import productService

app = Flask(__name__)
app.secret_key = 'mysecretkey'

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/node_modules/<path:path>')
def node_modules(path):
    return send_from_directory('node_modules', path)


@app.route('/')
def productlist():
    products = session.query(Product).all()
    return render_template("products.html", products=products)


@app.route('/product/<product_id>')
def productdetails(product_id):
    product = session.query(Product).get(product_id)
    return render_template("product.html", product=product)


@app.route('/newproduct', methods=['GET', 'POST'])
def addproduct():
    if request.method == 'POST':
        product = productService.create(request.form)
        name = product.name
        flash('New product %s successfully added!' % name)
        return redirect(url_for('addproduct'))
    else:
        categories = session.query(Category).all()
        return render_template("addProduct.html", categories=categories)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

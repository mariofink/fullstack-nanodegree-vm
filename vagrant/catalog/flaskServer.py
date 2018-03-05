from flask import Flask, request, render_template, redirect, url_for, flash, send_from_directory
import productService
import categoryService

app = Flask(__name__)
app.secret_key = 'mysecretkey'


@app.route('/node_modules/<path:path>')
def node_modules(path):
    return send_from_directory('node_modules', path)


@app.route('/')
def homepage():
    products = productService.recentlyAdded()
    categories = categoryService.all()
    return render_template("home.html", products=products, categories=categories)


@app.route('/product/<product_id>')
def productdetails(product_id):
    product = productService.get(product_id)
    return render_template("product.html", product=product)


@app.route('/product/<product_id>/delete', methods=['GET', 'POST'])
def deleteproduct(product_id):
    if request.method == 'POST':
        productService.delete(product_id)
        return redirect(url_for('homepage'))
    else:
        product = productService.get(product_id)
        return render_template("product-delete.html", product=product)


@app.route('/category/<category_id>')
def categorydetails(category_id):
    category = categoryService.get(category_id)
    products = categoryService.getProducts(category_id)
    return render_template("category.html", category=category, products=products)


@app.route('/newproduct', methods=['GET', 'POST'])
def addproduct():
    if request.method == 'POST':
        product = productService.create(request.form)
        name = product.name
        flash('New product %s successfully added!' % name)
        return redirect(url_for('addproduct'))
    else:
        categories = categoryService.all()
        return render_template("addProduct.html", categories=categories)


@app.route('/product/<product_id>/edit', methods=['GET', 'POST'])
def editproduct(product_id):
    product = productService.get(product_id)
    if request.method == 'POST':
        productService.update(product, request.form)
        flash('Saved changes to %s.' % product.name)
        return redirect("/")
    else:
        categories = categoryService.all()
        return render_template("editProduct.html", product=product, categories=categories)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

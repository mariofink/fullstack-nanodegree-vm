from flask import Flask, request, render_template, redirect, url_for, flash, \
    send_from_directory, jsonify
from flask import session as login_session
import random
import string
import productService
import categoryService
import authService
from forms import ItemForm, DeleteForm

app = Flask(__name__)
app.secret_key = 'mysecretkey'


@app.route('/node_modules/<path:path>')
def node_modules(path):
    """
    serve JS bundles from node_modules folder
    :param path:
    :return: resource requested in path
    """
    return send_from_directory('node_modules', path)


@app.route('/login')
def showLogin():
    """
    Create anti-forgery state token and attach it to the session
    :return:
    """
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    return render_template('login.html', login_session=login_session)


@app.route('/')
def homepage():
    """
    Render homepage with a list of all categories and recently added products
    :return:
    """
    products = productService.recentlyAdded()
    categories = categoryService.all()
    return render_template("home.html", products=products,
                           categories=categories, login_session=login_session)


@app.route('/product/<product_id>')
def productdetails(product_id):
    """
    Render the details of a single product
    :param product_id:
    :return:
    """
    product = productService.get(product_id)
    return render_template("product.html", product=product,
                           login_session=login_session)


@app.route('/product/<product_id>/delete', methods=['GET', 'POST'])
def deleteproduct(product_id):
    """
    For GET requests: render a form asking the user for confirmation
    For POST requests: remove a single product
    :param product_id:
    :return:
    """
    if 'username' not in login_session:
        flash("You are not authorised to delete products.")
        return redirect("/")

    form = DeleteForm(request.form)
    if request.method == 'POST' and form.validate():
        productService.delete(product_id)
        return redirect(url_for('homepage'))
    else:
        product = productService.get(product_id)
        return render_template("product-delete.html", product=product,
                               login_session=login_session, form=form)


@app.route('/category/<category_id>')
def categorydetails(category_id):
    """
    Render all products inside a specified category
    :param category_id:
    :return:
    """
    category = categoryService.get(category_id)
    products = categoryService.getProducts(category_id)
    return render_template("category.html", category=category,
                           products=products, login_session=login_session)


@app.route('/newproduct', methods=['GET', 'POST'])
def addproduct():
    """
    For GET requests, render a form to add new products
    For POST requests, validate the form data and create a new product
    :return:
    """
    if 'username' not in login_session:
        flash("You are not authorised to create new products.")
        return redirect("/")

    form = ItemForm(request.form)
    form.category.choices = categoryService.all_as_dict()
    if request.method == 'POST' and form.validate():
        product = productService.create(request.form)
        name = product.name
        flash('New product %s successfully added!' % name)
        return redirect(url_for('addproduct'))
    else:
        categories = categoryService.all()
        return render_template("addProduct.html", categories=categories,
                               login_session=login_session, form=form)


@app.route('/product/<product_id>/edit', methods=['GET', 'POST'])
def editproduct(product_id):
    """
    For GET requests, render a form to edit products
    For POST requests, validate the form data and store the changes
    :param product_id:
    :return:
    """
    if 'username' not in login_session:
        flash("You are not authorised to edit products.")
        return redirect("/")

    product = productService.get(product_id)
    form = ItemForm(request.form)
    form.category.choices = categoryService.all_as_dict()
    if request.method == 'POST' and form.validate():
        productService.update(product, request.form)
        flash('Saved changes to %s.' % product.name)
        return redirect("/")
    else:
        form.name.data = product.name
        form.description.data = product.description
        form.category.data = product.category_id
        return render_template("editProduct.html", product=product,
                               login_session=login_session, form=form)


@app.route('/api/v1/product/<product_id>')
def jsonifyProduct(product_id):
    """
    Return a single product in JSON format
    :param product_id:
    :return:
    """
    product = productService.get(product_id)
    serialised = product.serialize
    return jsonify(serialised)


@app.route('/api/v1/products')
def jsonifyProducts():
    """
    Return all products in JSON format
    :return:
    """
    products = productService.all()
    return jsonify(products=[i.serialize for i in products])


@app.route('/gconnect', methods=['POST'])
def gconnect():
    """
    Login with Google
    :return:
    """
    response = authService.gconnect(login_session)
    flash("You are now logged in as %s" % login_session['username'])
    return response


@app.route('/gdisconnect')
def gdisconnect():
    """
    Remove Google authentication
    :return:
    """
    if authService.gdisconnect(login_session):
        flash("You have been logged out.")
    else:
        flash("There was a problem logging you out.")
    return redirect("/")


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

from flask import Flask, request, render_template, redirect, url_for, flash, send_from_directory
import productService

app = Flask(__name__)
app.secret_key = 'mysecretkey'


@app.route('/node_modules/<path:path>')
def node_modules(path):
    return send_from_directory('node_modules', path)


@app.route('/')
def productlist():
    products = productService.all()
    categories = productService.getCategoryList()
    return render_template("home.html", products=products, categories=categories)


@app.route('/product/<product_id>')
def productdetails(product_id):
    product = productService.get(product_id)
    return render_template("product.html", product=product)


@app.route('/newproduct', methods=['GET', 'POST'])
def addproduct():
    if request.method == 'POST':
        product = productService.create(request.form)
        name = product.name
        flash('New product %s successfully added!' % name)
        return redirect(url_for('addproduct'))
    else:
        categories = productService.getCategoryList()
        return render_template("addProduct.html", categories=categories)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

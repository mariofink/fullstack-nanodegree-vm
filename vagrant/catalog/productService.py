from database_setup import Product, Category
import databaseService as db

"""Return a list of all products"""
def all():
    return db.session.query(Product).all()


"""Get a specific product by its primary key"""
def get(product_id):
    return db.session.query(Product).get(product_id)


"""Return a list of all categories"""
def getCategoryList():
    return db.session.query(Category).all()


"""Create a new product based on user input via POST request"""
def create(form):
    product = Product(name=form['name'], description=form['description'], category_id=form['category'])
    db.session.add(product)
    db.session.commit()
    return product

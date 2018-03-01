from database_setup import Product
import databaseService as db
from sqlalchemy import desc
import datetime


def all():
    """Return a list of all products"""
    return db.session.query(Product).all()


def get(product_id):
    """Get a specific product by its primary key"""
    return db.session.query(Product).get(product_id)


def recentlyAdded():
    """Return the last 10 recently added items"""
    return db.session.query(Product).order_by(desc(Product.created)).limit(10)


def create(form):
    """Create a new product based on user input via POST request"""
    product = Product(created=datetime.datetime.now(), name=form['name'], description=form['description'],
                      category_id=form['category'])
    db.session.add(product)
    db.session.commit()
    return product

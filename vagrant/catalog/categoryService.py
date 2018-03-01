from database_setup import Product, Category
import databaseService as db


def all():
    """Return a list of all categories"""
    return db.session.query(Category)


def get(category_id):
    """Get a specific category"""
    return db.session.query(Category).get(category_id)


def getProducts(category_id):
    """Get list of products in a specific category"""
    return db.session.query(Product).filter_by(category_id=category_id)

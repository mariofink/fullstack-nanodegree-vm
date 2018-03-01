from database_setup import Product
import databaseService as db


def create(form):
    product = Product(name=form['name'], description=form['description'], category_id=form['category'])
    db.session.add(product)
    db.session.commit()
    return product

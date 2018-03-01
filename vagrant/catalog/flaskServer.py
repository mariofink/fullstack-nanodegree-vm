from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Product, Category

app = Flask(__name__)

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
def productlist():
    products = session.query(Product).all()
    return render_template("products.html", products=products)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

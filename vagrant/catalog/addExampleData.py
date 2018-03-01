from database_setup import Product, Category, User
import databaseService as db

category1 = Category(name="My first category")
db.session.add(category1)
db.session.commit()

product1 = Product(name="My first product", description="Some nice description", category=category1)
db.session.add(product1)
db.session.commit()

user1 = User(userid="admin", name="Administrator", password="nimda")
db.session.add(user1)
db.session.commit()
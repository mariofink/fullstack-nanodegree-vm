from database_setup import Category, User
import databaseService as db
import productService

category1 = Category(name="My first category")
db.session.add(category1)
db.session.commit()

product1 = {
    'name': 'My first product',
    'description': 'Some nice description',
    'category': category1.id
}
productService.create(product1)

user1 = User(userid="admin", name="Administrator", password="nimda")
db.session.add(user1)
db.session.commit()

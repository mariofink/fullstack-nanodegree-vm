from database_setup import Category, User
import databaseService as db
import productService

snes = Category(name="Super Nintendo")
db.session.add(snes)

playstation = Category(name="Playstation")
db.session.add(playstation)

pc = Category(name="PC")
db.session.add(pc)

db.session.commit()

productService.create({
    'name': 'Super Mario World',
    'description': 'Best platformer ever!',
    'category': snes.id
})

productService.create({
    'name': "Donkey Kong Country",
    "description": "Go bananas",
    "category": snes.id
})

productService.create({
    "name": "NBA Jam",
    "description": "He's on fire!",
    "category": snes.id
})

productService.create({
    "name": "Tomb Raider",
    "description": "Dr. Jones? Never heard of him.",
    "category": playstation.id
})

productService.create({
    "name": "Populous",
    "description": "The original God-game",
    "category": pc.id
})

user1 = User(userid="admin", name="Administrator", password="nimda")
db.session.add(user1)
db.session.commit()

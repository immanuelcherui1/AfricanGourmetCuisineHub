from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData



metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    country = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(255))  # Path to the image file

    def __init__(self, title, ingredients, instructions, country, image=None):
        self.title = title
        self.ingredients = ingredients
        self.instructions = instructions
        self.country = country
        self.image = image

    def __repr__(self):
        return f"<Recipe {self.title}>"

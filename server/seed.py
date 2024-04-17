from faker import Faker
from app import db

from app import app

fake = Faker()


with app.app_context():
    # Delete existing records
    Recipes.query.delete()
 
   
    # Seed recipes
    

    print("Database seeded successfully!")

from faker import Faker
from server.models import Recipe
from server.models import db

fake = Faker()

def seed_database():
    with db.app.app_context():
        # Delete existing records
        db.session.query(Recipe).delete()

        # Seed recipes
        for _ in range(10):  # Seed 10 recipes
            title = fake.sentence()
            ingredients = "\n".join(fake.sentences(3))
            instructions = "\n".join(fake.sentences(5))
            area = fake.country()

            recipe = Recipe(title=title, ingredients=ingredients, instructions=instructions, area=area)
            db.session.add(recipe)

        db.session.commit()

        print("Database seeded successfully!")

if __name__ == "__main__":
    seed_database()

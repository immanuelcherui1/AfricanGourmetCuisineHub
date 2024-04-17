from models import db, UserProfile, Recipe, Review
from app import app

with app.app_context():
    # Delete existing records
    Recipe.query.delete()
    UserProfile.query.delete()
    Review.query.delete()


    def seed_data():
        #sample user profiles
        user1 = UserProfile(
            name="John Doe",
            email="john@gmail.com",
            password="password123"
        )
        user2 = UserProfile(
            name="Jane Doe",
            email="jane@gmail.com",
            password="password456"
        )

        #sample recipes with image paths
        recipe1 = Recipe(
            title="Pasta Carbonara",
            instructions="Lorem ipsum dolor sit amet.",
            category="Nyarwanda",
            country="Rwanda",
            image="images/pasta_carbonara.jpg",
            author=user1
        )
        recipe2 = Recipe(
            title="Mursik",
            instructions="Consectetur adipiscing elit.",
            category="Kalenjin",
            country="Kenyan",
            image="images/chicken_curry.jpg",
            author=user2
        )

        # sample reviews
        review1 = Review(
            comments="Delicious pasta!",
            rating=5,
            reviewer=user1,
            recipe=recipe1
        )
        review2 = Review(
            comments="Great curry recipe!",
            rating=4,
            reviewer=user2,
            recipe=recipe2
        )

        # sample data to the session and commit
        db.session.add_all([user1, user2, recipe1, recipe2, review1, review2])
        db.session.commit()

        print("Database seeded successfully!")

    seed_data()
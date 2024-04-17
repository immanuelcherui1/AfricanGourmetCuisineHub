from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, CheckConstraint
from sqlalchemy.orm import validates
from werkzeug.security import generate_password_hash, check_password_hash
from email_validator import validate_email, EmailNotValidError  


metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

# This is the association.
bookmarks = db.Table('bookmarks',
    db.Column('user_id', db.Integer, db.ForeignKey('user_profiles.id'), primary_key=True),
    db.Column('recipe_id', db.Integer, db.ForeignKey('recipes.id'), primary_key=True)
)

class UserProfile(db.Model):
    __tablename__ = 'user_profiles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    # Relationships
    recipes = db.relationship('Recipe', back_populates='author', lazy=True)  
    reviews = db.relationship('Review', back_populates='reviewer', lazy=True)  
    bookmarks = db.relationship('Recipe', secondary=bookmarks, lazy='subquery',
                                backref=db.backref('bookmarked_by', lazy=True))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    @validates('email')
    def validate_user_email(self, key, address):
        try:
            validate_email(address)
            return address
        except EmailNotValidError as e:
            raise ValueError("Invalid email address.")

class Recipe(db.Model):
    __tablename__ = 'recipes'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(100))
    image = db.Column(db.String(255))  #file path
    country = db.Column(db.String(100))

    user_id = db.Column(db.Integer, db.ForeignKey('user_profiles.id'))
    author = db.relationship('UserProfile', back_populates='recipes')  # Fixed back_populates

    reviews = db.relationship('Review', back_populates='recipe', lazy=True)

class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    comments = db.Column(db.Text)
    rating = db.Column(db.Integer) 

    user_id = db.Column(db.Integer, db.ForeignKey('user_profiles.id'))
    reviewer = db.relationship('UserProfile', back_populates='reviews')

    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'))
    recipe = db.relationship('Recipe', back_populates='reviews')

    # Add the CheckConstraint to the table arguments
    __table_args__ = (
        CheckConstraint('1 <= rating AND rating <= 5', name='rating_range'),
    )

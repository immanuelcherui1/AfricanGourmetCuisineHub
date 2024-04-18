#!/usr/bin/env python3

from flask import Flask, request, make_response, jsonify
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import ValidationError, fields
from email_validator import validate_email, EmailNotValidError
from flask_migrate import Migrate
from flask_restful import Api, Resource
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename
import os
from flask_cors import CORS

from models import db, UserProfile, Recipe, Review

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.json.compact = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['UPLOAD_FOLDER'] = 'UPLOAD_FOLDER'

CORS(app)

migrate = Migrate(app, db)
db.init_app(app)

ma = Marshmallow(app)

# Utility function to check file extension
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}


# Marshmallow Schemas
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserProfile
        load_instance = True
        exclude = ('password_hash',)
    
    name = ma.auto_field()
    email = ma.auto_field()

    url = ma.Hyperlinks(
        {
            "self": ma.URLFor(
                "userprofilesbyid",
                values=dict(id="<id>")),
            "collection": ma.URLFor("userprofiles"),
        }
    )

user_schema = UserSchema()
users_schema = UserSchema(many=True)

class RecipeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Recipe
    

recipe_schema = RecipeSchema()
recipes_schema = RecipeSchema(many=True)

class ReviewSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Review
        load_instance = True

review_schema = ReviewSchema()
reviews_schema = ReviewSchema(many=True)

class UserSignupSchema(ma.Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True)

user_signup_schema = UserSignupSchema()


# API Resources
api = Api(app)

class Index(Resource):

    def get(self):

        response_dict = {
            "index": " This is AGCH developed by a wonderful team: Immanuel, Linda, Mirriam & Sarah ",
        }

        response = make_response(
            response_dict,
            200,
        )

        return response

api.add_resource(Index, '/')

# Getting all Posts and posting to database
class RecipeList(Resource):
    # def get(self):
    #     return {'message': 'This route works!'}, 200

    def get(self):
        recipes = Recipe.query.all()
        # response = make_response(recipes_schema.dump(recipes)), 200
        return jsonify(recipes_schema.dump(recipes))


    def post(self):
        # Check for JSON data
        json_data = request.get_json()
        if not json_data:
            print("Group")
            return jsonify({'message': 'No input data provided'})
        
        # Validate and deserialize input
        try:
            data = recipe_schema.load(json_data)
        except ValidationError as err:
            return jsonify(err.messages), 422
        
        # Handle file upload
        if 'image' in request.files:
            image = request.files['image']
            if image.filename == '':
                return jsonify({'message': 'No selected file'}), 400
            if image and allowed_file(image.filename):
                filename = secure_filename(image.filename)
                image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                image.save(image_path)
                data['image'] = image_path  # Update the data dictionary with the image path
            else:
                return jsonify({'message': 'Invalid file type'}), 400

        # Create new Recipe instance
        recipe = Recipe(**data)
        db.session.add(recipe)
        db.session.commit()

        return recipe_schema.jsonify(recipe), 201

api.add_resource(RecipeList, '/recipes')


class RecipeDetail(Resource):
    def get(self, id):
        recipe = Recipe.query.filter_by(id=id).first()
        return recipe_schema.dump(recipe), 200

    def patch(self, id):
        recipe = Recipe.query.filter_by(id=id).first()
        for attr in request.form:
            setattr(recipe, attr, request.form[attr])
        db.session.commit()
        return recipe_schema.dump(recipe), 200

    def delete(self, id):
        recipe = Recipe.query.filter_by(id=id).first()
        db.session.delete(recipe)
        db.session.commit()
        return {'message': 'Recipe deleted'}, 200

api.add_resource(RecipeDetail, '/recipes/<int:id>')

# Define a new resource for searching recipes
class RecipeSearch(Resource):
    def get(self):
        # Get the search query from the request parameters
        search_query = request.args.get('q')

        # Search for recipes containing the search query
        recipes = Recipe.query.filter(Recipe.title.ilike(f'%{search_query}%')).all()

        if not recipes:
            return jsonify({'message': 'No recipes found. Showing similar results.'}), 404

        # Serialize the recipes and return the results
        return jsonify(recipes_schema.dump(recipes)), 200

# Add the new resource to the API
api.add_resource(RecipeSearch, '/recipes/search')

#  For Login
class UserPassword(Resource):
    def post(self):
        data = request.get_json()
        user = UserProfile.query.filter_by(email=data['email']).first()
        if user and check_password_hash(user.password_hash, data['password']):
            return {'message': 'Password matches'}, 200
        else:
            return {'message': 'Invalid password'}, 401


api.add_resource(UserPassword, '/login')

class UserSignup(Resource):
    def post(self):
        # Parse incoming JSON data
        json_data = request.get_json()
        
        # Validate JSON data against the schema
        try:
            validated_data = user_signup_schema.load(json_data)
        except ValidationError as err:
            return jsonify(err.messages)
        
        # Check if the email is already registered
        existing_user = UserProfile.query.filter_by(email=validated_data['email']).first()
        if existing_user:
            return jsonify({'message': 'Email already registered'})
        
        # Hash the password
        hashed_password = generate_password_hash(validated_data['password'])
        
        # Create a new user profile
        new_user = UserProfile(
            name=validated_data['name'],
            email=validated_data['email'],
            password_hash=hashed_password
        )
        
        # Add the user profile to the database
        db.session.add(new_user)
        db.session.commit()
        
        return jsonify({'message': 'User registered successfully'})

# Add the new resource to the API
api.add_resource(UserSignup, '/signup')


if __name__ == '__main__':
    app.run(port=5555, debug=True)

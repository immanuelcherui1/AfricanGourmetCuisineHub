from flask import Flask, jsonify, request, render_template
from flask_migrate import Migrate
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

# Serve your React application
@app.route('/')
def serve_frontend():
    return render_template('index.html')

# Route to display the form
@app.route('/submit_recipe_form')
def submit_recipe_form():
    return render_template('submit_recipe_form.html')

# Route to handle form submission and save data to the database
@app.route('/submit_recipe', methods=['POST'])
def submit_recipe():
    data = request.form  # Assuming form data is sent as form-urlencoded
    # Process the submitted recipe data and save to the database
    # Example:
    title = data.get('title')
    ingredients = data.get('ingredients')
    instructions = data.get('instructions')
    area = data.get('area')
    # Save data to the database using SQLAlchemy
    # Example: recipe = Recipe(title=title, ingredients=ingredients, instructions=instructions, area=area)
    # Example: db.session.add(recipe)
    # Example: db.session.commit()
    return jsonify({"message": "Recipe submitted successfully"}), 200

if __name__ == '__main__':
    app.run(port=5555, debug=True)

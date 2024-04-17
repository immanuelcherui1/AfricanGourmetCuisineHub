from flask import Flask, jsonify, request, render_template, send_from_directory
from flask_migrate import Migrate
from .models import db,Recipe
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

@app.route('/submit-recipe', methodS=['GET'])
def submit_recipe_form():
    return render_template('RecipeForm.jsx')

@app.route('/submit_recipe', methods=['POST'])
def submit_recipe():
    data = request.form
    file = request.files['image']
    filename = secure_filename(file.filename)
    if filename != '':
        file_path = os.path.join('path/to/save/images', filename)
        file.save(file_path)
    else:
        file_path = None

    new_recipe = Recipe(
        title=data.get('title'),
        ingredients=data.get('ingredients'),
        instructions=data.get('instructions'),
        country=data.get('country'),
        image=file_path
    )
    db.session.add(new_recipe)
    db.session.commit()
    return jsonify({"message": "Recipe submitted successfully"}), 200

if __name__ == '__main__':
    app.run(port=5555, debug=True)

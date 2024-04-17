from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create Flask application instance
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy instance
db = SQLAlchemy(app)

# Import routes after creating app to avoid circular import
# from server import models

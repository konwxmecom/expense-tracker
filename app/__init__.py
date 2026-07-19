from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# ⬇️ YEH LINE IMPORTANT HAI — db ko yahan define karo
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Database configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'dev-secret-key-change-in-production'
    
    # Database initialize karo
    db.init_app(app)
    
    # Home route
    @app.route('/')
    def home():
        return 'Expense Tracker API 🚀 Database connected!'
    
    return app
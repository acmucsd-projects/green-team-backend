from flask_sqlalchemy import SQLAlchemy

# Create db here to prevent circular dependencies with model files
db = SQLAlchemy()
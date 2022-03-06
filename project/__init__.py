import os
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    db.init_app(app)
    migrate.init_app(app, db)
    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}
    return app
from flask import Flask

from src.resources.pokemon import pokemonsRouting
from src.exceptions.error_handlers import register_error_handlers

def create_app():
    app = Flask(__name__)

    app.config.from_object('config.DevelopmentConfig')
    

    register_error_handlers(app)
    app.register_blueprint(pokemonsRouting)

    return app
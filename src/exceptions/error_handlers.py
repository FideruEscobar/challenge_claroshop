from flask import Flask, jsonify, make_response

from src.exceptions.custom_exceptions import PokeAPIError

def register_error_handlers(app):

    @app.errorhandler(400)
    def handle_bad_request(err):
        response = {"error": "Bad request"}
        app.logger.error(f"Message: {str(err)}")
        return make_response(jsonify(response), 400)

    @app.errorhandler(PokeAPIError)
    def handle_pokeapi_error(err):
        response = {"error": "Resource Not found"}
        app.logger.error(f"Message: {str(err)}")
        return make_response(jsonify(response), 404)


    @app.errorhandler(404)
    def handle_not_found_error(err):
        response = {"error": "Resource Not found"}
        app.logger.error(f"Message: {str(err)}")
        return make_response(jsonify(response), 404)

    @app.errorhandler(500)
    def handle_exception(err):
        response = {"error": "something failed"}
        app.logger.error(f"Unknown Exception: {str(err)}")
        return make_response(jsonify(response), 500)

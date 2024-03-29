from app import app
from flask import jsonify, abort, request
from tasks import example
from validators import MessageValidators
from pydantic import ValidationError


@app.route("/api/v1/sending_messages", methods=["POST"])
def sending_messages():
    try:
        data = request.json 
        MessageValidators(**data)
        message = data['message']
        response = {
            'message': message,
        }
        return response

    except ValidationError as e:
        response = {
            "error": f"{type(e).__name__}",
        }
        return response


@app.errorhandler(400)
def bad_request_error(error):
    message = {
        "error": f"{error}",
    }
    return jsonify(message), 400


@app.errorhandler(500)
def internal_error(error):
    message = {
        "error": f"{error}",
    }
    return jsonify(message), 500


@app.errorhandler(405)
def method_not_allowed(error):
    message = {
        "error": f"{error}",
    }
    return jsonify(message), 500


@app.errorhandler(404)
def not_found_error(error):
    message = {
        "error": f"{error}",
    }
    return jsonify(message), 404
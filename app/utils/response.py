from flask import jsonify

def error_response(message="An error occurred", errors=None, status_code=400):
    response = {
        'message': message,
        'errors': errors if errors else [],
        "status": "error",
        }
    return jsonify(response), status_code

def success_response(message="Success", data=None, status_code=200):
    response = {
        'message': message,
        'data': data,
        "status": "success",
        }
    return jsonify(response), status_code
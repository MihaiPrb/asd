from flask import request, jsonify
from functools import wraps
from jsonschema import validate, ValidationError

def validate_request(schema):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                data = request.get_json()
                validate(data, schema)
                return func(*args, **kwargs)
            except ValidationError as e:
                error_message = f"Invalid request data: {e.message}"
                return jsonify({'message': error_message}), 400
        return wrapper
    return decorator

# Example usage:
# @validate_request({
#     'type': 'object',
#     'properties': {
#         'name': {'type': 'string'},
#         'age': {'type': 'integer', 'minimum': 0},
#         'email': {'type': 'string', 'format': 'email'}
#     },
#     'required': ['name', 'age', 'email']
# })
# def example_route():
#     # Route logic here
#     pass
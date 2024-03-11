from functools import wraps
from flask import request, jsonify

def validate_request_data(required_fields):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            data = request.get_json()
            if data is None:
                return jsonify({'message': 'Invalid request data'}), 400
            for field in required_fields:
                if field not in data:
                    return jsonify({'message': f'Missing required field: {field}'}), 400
            return func(*args, **kwargs)
        return wrapper
    return decorator

def handle_exceptions(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return jsonify({'message': 'Internal server error', 'error': str(e)}), 500
    return wrapper
from flask import jsonify

def format_response(data=None, message=None, status_code=200):
    response = {}
    if message:
        response['message'] = message
    if data:
        response['data'] = data
    return jsonify(response), status_code

def success_response(data=None, message='Request successful', status_code=200):
    return format_response(data=data, message=message, status_code=status_code)

def error_response(message='An error occurred', status_code=400):
    return format_response(message=message, status_code=status_code)

def not_found_response(message='Resource not found', status_code=404):
    return format_response(message=message, status_code=status_code)

def unauthorized_response(message='Unauthorized access', status_code=401):
    return format_response(message=message, status_code=status_code)

def forbidden_response(message='Forbidden access', status_code=403):
    return format_response(message=message, status_code=status_code)

# Example usage:
# @app.route('/example')
# def example_route():
#     data = {'name': 'John Doe', 'age': 25}
#     return success_response(data=data)
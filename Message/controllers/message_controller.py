from flask import request, jsonify
from services.message_service import MessageService
from flask.views import MethodView
import jwt
import config

class MessageView(MethodView):
    def __init__(self):
        self.message_service = MessageService()

    def extract_user_id(self, token):
        try:
            decoded_token = jwt.decode(token, config.JWT_SECURITY_KEY, algorithms=["HS256"])
            user_id = decoded_token.get('user_id')
            return user_id
        except jwt.ExpiredSignatureError:
            # TODO: Handle token expiration error
            return None
        except jwt.InvalidTokenError:
            # TODO: Handle invalid token error
            return None

    def post(self):
        token = request.headers.get('Authorization').split()[1]  # "Bearer <token>"
        if not token:
            return jsonify({'error': 'Authorization token is missing'}), 401

        # TODO: Implement JWT token validation

        message_data = request.json
        if not message_data:
            return jsonify({'error': 'Request data is missing or invalid'}), 400

        user_id = self.extract_user_id(token)
        if not user_id:
            return jsonify({'error': 'Invalid token'}), 401

        result = self.message_service.create_message(user_id, message_data)
        return jsonify(result)



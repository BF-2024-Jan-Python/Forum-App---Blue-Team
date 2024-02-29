from datetime import datetime

from flask import jsonify, request
from flask.views import MethodView

from aop.decorators import token_required
from models.history import History
from services.history_service import HistoryService


class HistoryController(MethodView):
    def __init__(self):
        self.history_service = HistoryService()

    # @token_required
    def get(self, user_id):

        history_result = self.history_service.get_history_by_user(user_id)
        if not history_result:
            return jsonify(history_result)
        print(history_result[0].serialize())

        return jsonify([res.serialize() for res in history_result])

    # @token_required
    def post(self, user_id):
        try:
            post_id = request.json['postId']
        except KeyError:
            return jsonify({'message': 'postId is missing in request'}), 400

        history_data = {
            'userId': user_id,
            'postId': post_id,
            'viewDate': datetime.utcnow()
        }

        success, message = self.history_service.create_history(history_data)

        if success:
            return jsonify({'message': message, 'uid': history_data['userId']}), 201
        else:
            return jsonify({'message': message}), 400
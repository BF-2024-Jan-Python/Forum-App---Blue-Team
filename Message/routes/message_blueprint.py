from flask import Blueprint
from controllers.message_controller import MessageView

message_blueprint = Blueprint('message', __name__)

message_blueprint.add_url_rule('/message/', view_func=MessageView.as_view('message'), methods=['POST'])
from datetime import datetime
from repos.message_repo import MessageRepository

class MessageService:
    def __init__(self):
        self.message_repository = MessageRepository()

    def create_message(self, user_id, message_data):
        message = message_data.get('message')
        email = message_data.get('email')
        date_created = datetime.utcnow()
        status = 'Open'

        result = self.message_repository.save_message(user_id, email, message, date_created, status)
        return result

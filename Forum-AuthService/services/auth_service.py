import datetime
import config
import pika
import jwt

from repos.auth_repo import AuthRepository
from models.auth import Auth


class AuthService:
    def __init__(self, rabbitmq_host='localhost'):

        self.auth_repository = AuthRepository()

        self.rabbitmq_host = rabbitmq_host
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.rabbitmq_host))
        self.channel = self.connection.channel()

        self.channel.queue_declare(queue='verification_code_queue')
        self.channel.queue_declare(queue='email_queue')
        self.channel.basic_consume(queue='verification_code_queue', on_message_callback=self.process_verification_code, auto_ack=True)

    def process_verification_code(self, ch, method, properties, body):
        data = body.decode('utf-8').split(',')
        user_id, verification_code = data[0], data[1]

        # set db here -----
        self.auth_repository.set_verification_code(user_id, verification_code)

        print("Received verification code:")
        print("Receiver ID:", user_id)
        print("Verification Code:", verification_code)

    def start_listening(self):
        print('Auth service started listening for verification codes from RabbitMQ...')
        self.channel.start_consuming()

    def send_email_to_queue(self, receiver_email, user_id):

        message = f'{user_id}{receiver_email}'
        self.channel.basic_publish(exchange='', routing_key='email_queue', body=message)
        print("Message sent to RabbitMQ queue")

        return {"message": "User email sent to RabbitMQ queue."}

    def set_user_token(self, user_id):
        expiration_time = datetime.datetime.utcnow() + datetime.timedelta(minutes=10000)
        token_payload = {'user_id': user_id, 'exp': expiration_time}
        jwt_secret_key = config.JWT_SECURITY_KEY
        token = jwt.encode(token_payload, jwt_secret_key, algorithm="HS256")

        print("User token created: ", user_id, token)
        self.auth_repository.add_user(user_id)
        self.auth_repository.set_auth_token(user_id, token)

        return {"user_id": user_id, "token":token}
    
    def verify_user_token(self, user_id, token):
        if self.auth_repository.get_token_by_user_id(user_id) == token:
            return {"verification_result": True}
        else:
            return {"verification_result": False}
    
    def verify_user_code(self, user_id, verification_code):
        if self.auth_repository.get_verification_code_by_user_id(user_id) == verification_code:
            return {"verification_result": True}
        else:
            return {"verification_result": False}
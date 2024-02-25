from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models.message import db


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://admin:Danmoai0?JWJ@team-blue-database.cbagagysshae.us-east-2.rds.amazonaws.com/Message_DB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    # Create database tables
    db.create_all()

if __name__ == '__main__':
    # to resolve circular import issue
    from routes.message_blueprint import message_blueprint
    app.register_blueprint(message_blueprint)

    app.run(debug=True, port=6008)

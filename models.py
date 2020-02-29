from app import app
from flask_sqlalchemy import SQLAlchemy


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)


class LogRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    log_type = db.Column(db.String(20), unique=False,
                         nullable=False, index=True)
    value = db.Column(db.Float, unique=False, nullable=False)
    timestamp = db.Column(db.Integer, nullable=False, index=True)

    def __repr__(self):
        return '({type}, {value}, {time})'.format(type=self.log_type, value=self.value, time=self.timestamp)

from datetime import datetime
from app import db

class Task(db.Model):

    __tablename__ = 'Tasks'

    pid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text(100), nullable=False)
    description = db.Column(db.Text(200))
    status = db.Column(db.Text(20), default='pending')
    # deadline = db.Column(db.DateTime)

    def __repr__(self):
        return f"Task(pid={self.pid}, name='{self.name}', status='{self.status}')"

    # def save_to_db(self):
    #     db.session.add(self)
    #     db.session.commit()

    # def delete_from_db(self):
    #     db.session.delete(self)
    #     db.session.commit()
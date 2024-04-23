from datetime import datetime
from app import db

class Task(db.Model):

    __tablename__ = 'Tasks'

    pid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text(100), nullable=False)
    description = db.Column(db.Text(200))
    status = db.Column(db.Text(20), default='pending')

    def __repr__(self):
        """
        Return a string representation of the Task object.

        Returns:
            str: A string representing the Task object, including its ID, name, and status.
        """
        return f"Task(pid={self.pid}, name='{self.name}', status='{self.status}')"

    def save_to_db(self):
        """
        Save the current object to the database.

        Adds the current object to the database session and commits the transaction.
        """
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        """
        Remove the current object from the database.

        Delete the current object from the database session and commits the transaction.
        """
        db.session.delete(self)
        db.session.commit()
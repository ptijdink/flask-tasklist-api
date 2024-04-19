from typing import Optional
from datetime import datetime

class Task:
    _id_counter = 1

    def __init__(self, name: str, description: str, status: str, deadline: Optional[datetime] = None) -> None:
        """
        Initialize a new Task object.

        Args:
            name (str): The name of the task.
            description (str): The description of the task.
            status (str): The status of the task (e.g., 'pending', 'in progress', 'completed').
            deadline (Optional[datetime]): The deadline for the task (optional).

        Returns:
            None
        """       
        self.id = f"{Task._id_counter:03d}"
        self.name = name
        self.description = description
        self.status = status
        self.deadline = deadline

        Task._id_counter += 1


    def __repr__(self) -> str:
        """
        Return a string representation of the Task object.

        Returns:
            str: A string representing the Task object, including its ID, name, and status.
        """
        return f"Task(id={self.id}, name='{self.name}', status='{self.status}')"
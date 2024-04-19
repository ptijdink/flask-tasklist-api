import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.models.task import Task  

class TestTask(unittest.TestCase):
    def test_auto_generated_id(self):
        """Test auto-generated IDs for tasks.

        Create two tasks and check if the IDs are correctly formatted with at least three digits.
        and if the counter increments properly.
        """
        task1 = Task("Do the laundry", "Wash clothes", "in progress")
        task2 = Task("Buy groceries", "Get eggs, milk, and bread", "pending")

        self.assertEqual(len(task1.id), 3)
        self.assertEqual(task2.id, f"{2:03d}")

    def test_task_repr(self):
        """Test the __repr__ method of the Task class.

        Create a task and check if the __repr__ method returns the correct string representation.
        """
        task = Task("Do the laundry", "Wash clothes", "in progress")

        self.assertEqual(repr(task), "Task(id=003, name='Do the laundry', status='in progress')")


if __name__ == "__main__":
    unittest.main()
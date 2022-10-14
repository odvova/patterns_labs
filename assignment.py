from __future__ import annotations

from project import Project
from dataclasses import dataclass
from _datetime import datetime
from typing import Dict, List


class Task:
    """Task contains common info about tasks
        Attributes:
            title (str): Task title.
            status (str): is_done/0%.
            deadline (datetime): Term to complete a task
            items (List[str]): ???
            related_project (str): Concrete project related to concrete employee
    """
    def __init__(self, title: str, status: str):
        self.title = title
        self.status = status
        self.deadline: datetime
        self.items: List[str]
        self.related_project: str

    def implement_item(self, item_name: str):
        pass


class Assignment:
    """Assignment as the container for tasks.
    Related to Developer, QAEngineer and ProjectManager classes.

    Attributes:
        received_tasks (Dict): dictionary in form of
                        {date1: task1, date2: task2,...}.
                        Here date1, date2, ... are strings from datetime.
                        E.g., d = datetime.now(); d = d.strftime("%m/%d/%Y")
        is_done (bool): True, if all tasks are completed.
        description (str): General assignment description.
        status (str): Percent of completed tasks.

    """

    def __init__(self, description: str) -> None:
        """Assignment initializer."""
        self.description = description
        self.received_tasks = {Task}
        self.status = ""
        self.is_done = False

    def get_tasks_to_date(self, date: str) -> List[Task]:
        """Returns all tasks before date in arguments.

        Arguments:
            date (str): should be in format of '09/23/2022'!.

        Returns:
            List of tasks.

        """
        date_to_compare = datetime.strptime(date, "%m/%d/%Y")
        # List comprehension
        return [v for k, v in self.received_tasks.items()
                if datetime.strptime(k, "%m/%d/%Y") < date_to_compare]

    def calculate_status(self) -> None:
        """Calculates percentage of implemented tasks.

        Arguments:
            None.
        """
        tasks = [task for _, task in self.received_tasks.items()
                 if task["is_done"]]
        if tasks:
            self.status = str(100 * len(tasks) / len(self.received_tasks)) + "%"
        else:
            self.status = str("0%")


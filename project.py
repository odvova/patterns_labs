"""Contains assignments, tasks and Project implementation.

class Project
class Assignment

"""

from __future__ import annotations
from typing import Dict, List, TYPE_CHECKING
from datetime import datetime
if TYPE_CHECKING:
    from employees import Developer


class Project:
    """Project representation.

    Attributes:
        title (str): Project's name.
        start_date (str): Start date.
        tasks_list (List): list of all tasks related to project.
        developers (List[Developer]): List of assigned developers.
        limit (int): specifies maximum number of workers.

    """

    def __init__(self, title: str, limit: int) -> None:
        """Project initializer."""
        self.title: str = title
        self.start_date: str = datetime.now().strftime("%m/%d/%Y")
        self.tasks_list: List[Dict] = []
        self.developers: List[Developer] = []
        self.limit: int = limit

    def add_developer(self, developer: Developer) -> None:
        """Assigns developer to project instance.

        Args:
            developer (Developer): Concrete developer to be assigned.

        Returns:
            None.

        """
        try:
            developer.assign(project=self)
        except ValueError:
            print(f"Developer {developer.full_name} exists")
        self.developers.append(developer)

    def remove_developer(self, developer: Developer) -> None:
        """Removes developer from project instance.

        Args:
            developer (Developer): Concrete developer to be removed.

        Returns:
            None.

        """
        developer.unassign(project=self)
        self.developers.remove(developer)


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
        self.description: str = description
        self.received_tasks: Dict = {}
        self.status: str = ""
        self.is_done = False

    def get_tasks_to_date(self, date: str) -> List:
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
            self.status = str(100 * len(tasks)/len(self.received_tasks)) + "%"
        else:
            self.status = str("0%")

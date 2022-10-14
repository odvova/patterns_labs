"""Contains assignments, tasks and Project implementation.

class Project
class Assignment

"""

from __future__ import annotations

import uuid
from typing import Dict, List, TYPE_CHECKING
from collections import defaultdict
from datetime import datetime

if TYPE_CHECKING:
    from employees import Employee


class AssignmentManager:
    """Links concrete employee via multiple one to many"""

    def __init__(self) -> None:
        """Initializes assignment logic"""
        self.employee_projects = defaultdict(list)
        self.project_employees = defaultdict(list)

    def link(self, employee_id: uuid.UUID, project_title: str) -> None:
        """"""
        if employee_id not in self.employee_projects:
            self.employee_projects[employee_id].append(project_title)
            self.project_employees[project_title].append(employee_id)
        else:
            raise ValueError(f"Provided employee ID exists")

    def unlink(self, employee_id: uuid.UUID, project_title: str) -> None:
        """Add docstring!!!"""
        if employee_id in self.employee_projects:
            self.employee_projects[employee_id].remove(project_title)
            self.project_employees[project_title].remove(employee_id)
        else:
            raise ValueError(f"Nothing to remove")

    def get_project_title(self, employee_id: uuid.UUID) -> List[str]:
        return self.employee_projects[employee_id]


class Project:
    """Project representation.

    Attributes:
        title (str): Project's name.
        start_date (str): Start date.
        limit (int): specifies maximum number of workers.

    """

    def __init__(self, title: str, limit: int) -> None:
        """Project initializer."""
        self.title = title
        self.start_date = datetime.now().strftime("%m/%d/%Y")
        self.tasks_list: List[Dict]
        self.limit = limit

    def add_employee(self, employee: Employee, manager: AssignmentManager) -> None:
        """Assigns employee to project instance.

        Args:
            manager (AssignmentManager): Assigns concrete employee.
            employee (Employee): Concrete employee to be assigned.

        Returns:
            None.
        """
        manager.link(employee_id=employee.id, project_title=self.title)

    def remove_developer(self, employee: Employee, manager: AssignmentManager) -> None:
        """Removes employee from project instance.

        Args:
            manager (AssignmentManager): Unassigns concrete employee.
            employee (Employee): Concrete employee to be removed.

        Returns:
            None.

        """
        manager.unlink(employee_id=employee.id, project_title=self.title)




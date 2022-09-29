"""Contains Developer, QAEngineer and PM implementation.

class Developer
class QAEngineer
class ProjectManager

"""

from __future__ import annotations
import itertools
from typing import List, TYPE_CHECKING, Tuple, Set

if TYPE_CHECKING:
    from project import Project, Assignment


class Developer:
    """Developer representation.

    Attributes:
        _id (int): Developers ID, is incremented for each instance.
        full_name (str): First + last names.
        address (str): Registration address.
        email (str): Personal company e-mail.
        phone_number (str) : Person's working phone number.
        position (str): Persons company position (e.g., 'Junior').
        salary (str): Salary amount (can be re-calculated).
        projects (List[Projects]): List of assigned projects
                            (many-to-many with Project instance).
        assignments (List[Assignment]): List of assigned tasks in
                                    Assignment container.

    """

    id_iter = itertools.count()

    def __init__(self, full_name: str, address: str, email: str,
                 phone_number: str, position: str, salary: str, projects: List[Project], assignments: List[Assignment]) -> None:
        """Developer's initializer.
        """
        self._id = next(self.id_iter)
        self.full_name = full_name
        self.address = address
        self.email = email
        self.phone_number = phone_number
        self.position = position
        self.salary = salary
        self.projects = []
        self.assignments = []

    def get_assigned_projects(self) -> List[str]:
        """Returns all project titles assigned to developer.

         Arguments:
            None.

        Returns:
            List[str], list of project titles

        """
        return [project.title for project in self.projects]

    def assign(self, project: Project) -> None:
        """Assigns current developer to project instance.

        Args:
            project (Project): Project instance to be assigned to developer.

        Returns:
            None.

        """
        if project in self.projects:
            raise ValueError("Project {project.title} already exists")
        self.projects.append(project)
        print("Project {project.title} has been added to developer ", {self.full_name})

    def unassign(self, project: Project) -> None:
        """Assigns current developer to project instance.

        Arguments:
            project (Project): Project instance to be removed from developer.

        Returns:
            None.

        """
        if project in self.projects:
            self.projects.remove(project)
            print("Project", {project.title}, "has been removed from developer", {self.full_name})

    def __str__(self):
        """String representation of the Developer"""
        return "Developer", {self.full_name}


class QAEngineer:
    """QA engineer representation.

    Attributes:
        _id (int): QAEngineer ID, is incremented for each instance.
        full_name (str): First + last names.
        address (str): Registration address.
        email (str): Personal company e-mail.
        phone_number (str) : Person's working phone number.
        position (str): Persons company position (e.g., 'Junior').
        salary (str): Salary amount (can be re-calculated).
        projects (List[Projects]): List of assigned projects
                        (many-to-many with Project instance).

    """

    id_iter = itertools.count()

    def __init__(self, full_name: str, address: str, email: str,
                 phone_number: str, position: str, salary: str, projects: List[Project]) -> None:
        """QAEngineer's initializer.
        """
        self._id = next(self.id_iter)
        self.full_name = full_name
        self.address = address
        self.email = email
        self.phone_number = phone_number
        self.position = position
        self.salary = salary
        self.projects = []

    def test_feature(self, assignment: Assignment) -> Tuple[str, Set[str]]:
        """Simply the stub method, will be implemented in the future.

        Arguments:
            assignment (Assignment): assignment obtained from the developer.

        Returns:
            String contains dummy info about testing:).
        """
        return "Assignment {assignment.description} has been tested by", {self.full_name}


class ProjectManager:
    """Project manager representation.

    Attributes:
        _id (int): PM's ID, is incremented for each instance.
        full_name (str): First + last names.
        address (str): Registration address.
        email (str): Personal company e-mail
        phone_number (str) : Person's working phone number.
        position (str): Persons company position (e.g., 'Junior').
        salary (str): Salary amount (can be re-calculated).
        project (Projects): Assume PM -> Project relation.

    """

    id_iter = itertools.count()

    def __init__(self, full_name: str, address: str, email: str,
                 phone_number: str, position: str, salary: str,
                 project: Project) -> None:
        """ProjectManager initializer.
        """
        self._id = next(self.id_iter)
        self.full_name = full_name
        self.address = address
        self.email = email
        self.phone_number = phone_number
        self.position = position
        self.salary = salary
        self.project = project

    def discuss_progress(self, developer: Developer) -> Tuple[str, Set[str]]:
        """Simply the stub method, will be implemented in the future.

        Arguments:
            developer (Developer): Processing the developer's progress.

        Returns:
            String contains dummy discussion:).

        """

        # Let's obtain each assignment description.
        descriptions = [assignment.description for assignment in developer.assignments]
        # concat list of strings (descriptions) into one string
        descriptions = " ".join(descriptions)
        return "Task's progress of {descriptions} has been tested by", {self.full_name}

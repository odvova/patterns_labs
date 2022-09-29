"""Contains Developer, QAEngineer and PM implementation.

class Developer
class QAEngineer
class ProjectManager

"""

from __future__ import annotations
import itertools
from typing import List, TYPE_CHECKING
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
                 phone_number: str, position: str, salary: str) -> None:
        """Developer's initializer.
        """
        self._id = next(self.id_iter)
        self.full_name: str = full_name
        self.address: str = address
        self.email: str = email
        self.phone_number: str = phone_number
        self.position: str = position
        self.salary: str = salary
        self.projects: List[Project] = []
        self.assignments: List[Assignment] = []

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
            raise ValueError(f"Project {project.title} already exists")
        self.projects.append(project)
        print(f"Project {project.title} has been added to developer "
              f"{self.full_name}")

    def unassign(self, project: Project) -> None:
        """Assigns current developer to project instance.

        Arguments:
            project (Project): Project instance to be removed from developer.

        Returns:
            None.

        """
        if project in self.projects:
            self.projects.remove(project)
            print(f"Project {project.title} has been removed from developer {self.full_name}")

    def __str__(self):
        """String representation of the Developer"""
        return f"Developer {self.full_name}"


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
                 phone_number: str, position: str, salary: str) -> None:
        """QAEngineer's initializer.
        """
        self._id = next(self.id_iter)
        self.full_name: str = full_name
        self.address: str = address
        self.email: str = email
        self.phone_number: str = phone_number
        self.position: str = position
        self.salary: str = salary
        self.projects: List[Project] = []

    def test_feature(self, assignment: Assignment) -> str:
        """Simply the stub method, will be implemented in future.

        Arguments:
            assignment (Assignment): assignment obtained from the developer.

        Returns:
            String contains dummy info about testing:).
        """
        return f"Assignment {assignment.description} has been tested " \
               f"by {self.full_name}"


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
        self.full_name: str = full_name
        self.address: str = address
        self.email: str = email
        self.phone_number: str = phone_number
        self.position: str = position
        self.salary: str = salary
        self.project: project = project

    def discuss_progress(self, developer: Developer) -> str:
        """Simply the stub method, will be implemented in future.

        Arguments:
            developer (Developer): Processing the developer's progress.

        Returns:
            String contains dummy discussion:).

        """

        # Let's obtain each assignment description.
        descriptions = [assignment.description for assignment in developer.assignments]
        # concat list of strings (descriptions) into one string
        descriptions = " ".join(descriptions)
        return f"Task's progress of {descriptions} has been tested " \
               f"by {self.full_name}"

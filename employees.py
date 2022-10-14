"""Contains Developer, QAEngineer and PM implementation.

class Developer
class QAEngineer
class ProjectManager

"""

from __future__ import annotations
from dataclasses import dataclass
from abc import ABC, abstractmethod
import itertools
import uuid
from typing import List, TYPE_CHECKING, Tuple, Set

if TYPE_CHECKING:
    from project import Project, Assignment


@dataclass
class PersonalInfo:
    """Common info representation"""
    full_name: str
    address: str
    email: str
    phone_number: str
    position: str
    salary: str

    @property
    def first_name(self) -> str:
        return self.full_name.split()[0]

    def last_name(self) -> str:
        return self.full_name.split()[1]


class Employee(ABC):
    """Generic representation of employees"""

    def __init__(self, full_name: str, address: str, email: str, phone_number: str, position: str, salary: str) -> None:
        """Initialises Employee, creates Personal info object"""
        self._id = uuid.uuid4()
        self.personal_info = PersonalInfo(
            full_name=full_name,
            address=address,
            email=email,
            phone_number=phone_number,
            position=position,
            salary=salary
        )

    @abstractmethod
    def calculate_salary(self, assignment_manager) -> float:
        """Calculates and returns value in a salary attribute"""
        pass

    @abstractmethod
    def ask_sick_leave(self, project_manager: ProjectManager) -> bool:
        """???"""
        pass

    @property
    def id(self):
        return self._id


class Developer(Employee):
    """Developer representation.

    Attributes:
        _id (int): Developers ID, is incremented for each instance.
         full_name (str): First + last names.
        address (str): Registration address.
        email (str): Personal company e-mail.
        phone_number (str) : Person's working phone number.
        position (str): Persons company position (e.g., 'Junior').
        salary (str): Salary amount (can be re-calculated).
        assignments (List[Assignment]): List of assigned tasks in
                                    Assignment container.

    """

    id_iter = itertools.count()

    def __init__(self, full_name: str, address: str, email: str,
                 phone_number: str, position: str, salary: str) -> None:
        """Developer's initializer.

            Returns:
                None
        """
        self._id = next(self.id_iter)
        super().__init__(full_name=full_name,
                         address=address,
                         email=email,
                         phone_number=phone_number,
                         position=position,
                         salary=salary)
        self.assignments: List[Assignment] = []

    def calculate_salary(self, assignment_manager) -> float:
        """Returns employees salary
            Args:
                assignment_manager: obtains number of projects done by employee
            Returns:
                float
        """
        project_number = len(assignment_manager.get_project_title(self._id))
        return project_number * 100

    def ask_sick_leave(self, project_manager: ProjectManager) -> bool:
        """???"""
        pass

    def __str__(self):
        """String representation of the Developer"""
        return "Developer", {self.personal_info.full_name}


class QAEngineer(Employee, ABC):
    """QA engineer representation.

    Attributes:
        _id (int): QAEngineer ID, is incremented for each instance.
        full_name (str): First + last names.
        address (str): Registration address.
        email (str): Personal company e-mail.
        phone_number (str) : Person's working phone number.
        position (str): Persons company position (e.g., 'Junior').
        salary (str): Salary amount (can be re-calculated).

    """
    id_iter = itertools.count()

    def __init__(self, full_name: str, address: str, email: str,
                 phone_number: str, position: str, salary: str) -> None:
        """QAEngineer's initializer.
        """
        self._id = next(self.id_iter)
        super().__init__(full_name=full_name,
                         address=address,
                         email=email,
                         phone_number=phone_number,
                         position=position,
                         salary=salary)
        self.assignments: List[Assignment] = []

    def ask_sick_leave(self, project_manager: ProjectManager) -> bool:
        """???"""
        pass

    def add_ticket(self) -> None:
        pass

    def test_feature(self, assignment: Assignment) -> str:
        """Simply the stub method, will be implemented in the future.

        Arguments:
            assignment (Assignment): assignment obtained from the developer.

        Returns:
            String contains dummy info about testing:).
        """
        return f"Assignment {assignment.description} has been tested by {self.personal_info.full_name}"


class ProjectManager(Employee, ABC):
    """Project manager representation.

    Attributes:
        _id (int): PM's ID, is incremented for each instance.
        full_name (str): First + last names.
        address (str): Registration address.
        email (str): Personal company e-mail
        phone_number (str) : Person's working phone number.
        position (str): Persons company position (e.g., 'Junior').
        salary (str): Salary amount (can be re-calculated).

    """

    id_iter = itertools.count()

    def __init__(self, full_name: str, address: str, email: str,
                 phone_number: str, position: str, salary: str) -> None:
        """PM's initializer.
            Args:
                full_name (str): First + last names.
                address (str): Registration address.
                email (str): Personal company e-mail.
                phone_number (str) : Person's working phone number.
                position (str): Persons company position (e.g., 'Junior').
                salary (str): Salary amount (can be re-calculated).
            Returns:
                None
        """
        self._id = next(self.id_iter)
        super().__init__(full_name=full_name,
                         address=address,
                         email=email,
                         phone_number=phone_number,
                         position=position,
                         salary=salary)

    def calculate_salary(self, assignment_manager) -> float:
        """Returns employees salary
            Args:
                assignment_manager: obtains number of projects done by employee
            Returns:
                float
        """
        project_number = len(assignment_manager.get_project_title(self._id))
        return project_number * 100

    def ask_sick_leave(self, project_manager: ProjectManager) -> bool:
        """"""
        pass

    def discuss_progress(self, employee: Employee) -> Tuple[str, Set[str]]:
        pass

from employees import Developer
from unittest.mock import Mock


class TestDeveloper:
    def test_get_assigned(self,):
        mock = Mock()
        mock.title = "test"
        dev = Developer("name", "address", "email", "12345", "1", "test")
        dev.projects.append(mock)
        assert dev.get_assigned_projects() == ["test"]

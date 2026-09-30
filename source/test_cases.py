"""
/****************/
Mã sinh viên: 202419016
Họ tên: Phạm Xuân Việt
/****************/
"""

import contextlib
import io
import unittest
from employee import Employee
from software_engineer import SoftwareEngineer
from project_team import ProjectTeam


class TestProjectTeam(unittest.TestCase):
    def setUp(self):
        # Giữ kết quả kiểm thử gọn, không in các thông báo vòng đời.
        self.output = contextlib.redirect_stdout(io.StringIO())
        self.output.__enter__()
        self.addCleanup(self.output.__exit__, None, None, None)

    def test_default_employee(self):
        employee = Employee()
        self.assertEqual((employee.id, employee.fullName, employee.baseSalary),
                         ("UNKNOWN", "Unnamed employee", 0))

    def test_empty_id_and_name(self):
        for id, name in [("", "An"), ("  ", "An"), ("NV01", " ")]:
            with self.assertRaises(ValueError):
                Employee(id, name)

    def test_invalid_salary(self):
        for salary in [-1, float("nan"), float("inf")]:
            with self.assertRaises(ValueError):
                Employee("NV01", "An", salary)

    def test_salary_overloads(self):
        employee = Employee("NV01", "An", 10000000)
        employee.increaseSalary(1000000)
        employee.increaseSalary(10, True)
        employee.increaseSalary(900000, False)
        self.assertAlmostEqual(employee.baseSalary, 13000000)

    def test_invalid_raise_does_not_change_salary(self):
        employee = Employee("NV01", "An", 100)
        for value in [0, -1, float("nan"), float("inf")]:
            with self.assertRaises(ValueError):
                employee.increaseSalary(value)
        self.assertEqual(employee.baseSalary, 100)

    def test_engineer_constructors_and_cost(self):
        first = SoftwareEngineer("KS01", "Nam", "Python")
        second = SoftwareEngineer("KS02", "Linh", 15000000, "C#", 2000000)
        self.assertEqual(first.calculateMonthlyCost(), 0)
        self.assertEqual(second.calculateMonthlyCost(), 17000000)

    def test_invalid_engineer(self):
        for args in [(" ",), (10, "Python", -1), (10, "Python", float("nan"))]:
            with self.assertRaises(ValueError):
                SoftwareEngineer("KS01", "Nam", *args)
        with self.assertRaises(TypeError):
            SoftwareEngineer("KS01", "Nam")

    def test_empty_team(self):
        with ProjectTeam("DA01", "Dự án") as team:
            self.assertIsNone(team.leader)
            self.assertEqual(team.members, ())
            self.assertEqual(team.calculateTotalMonthlyCost(), 0)
            self.assertFalse(team.removeMember("KHONG_CO"))

    def test_constructor_adds_leader_once(self):
        leader = Employee("NV01", "An")
        with ProjectTeam("DA01", "Dự án", leader) as team:
            self.assertEqual(team.members, (leader,))
            self.assertFalse(team.addMember(leader, True))
            self.assertIs(team.leader, leader)

    def test_duplicate_id(self):
        first, other = Employee("NV01", "An"), Employee("NV01", "Bình")
        with ProjectTeam("DA01", "Dự án", first) as team:
            self.assertFalse(team.addMember(other))
            self.assertFalse(team.changeLeader(other))
            self.assertEqual(team.members, (first,))

    def test_change_and_remove_leader(self):
        first, second = Employee("NV01", "An"), Employee("NV02", "Hà")
        with ProjectTeam("DA01", "Dự án", first) as team:
            self.assertFalse(team.removeMember(first.id))
            self.assertTrue(team.changeLeader(second))
            self.assertEqual(len(team.members), 2)
            self.assertTrue(team.contains(first.id))
            self.assertTrue(team.removeMember(first.id))
            self.assertIs(team.leader, second)

    def test_add_new_leader_keeps_old_leader(self):
        first, second = Employee("NV01", "An"), Employee("NV02", "Hà")
        with ProjectTeam("DA01", "Dự án", first) as team:
            self.assertTrue(team.addMember(second, True))
            self.assertIs(team.leader, second)
            self.assertTrue(team.contains(first.id))

    def test_polymorphic_total(self):
        employee = Employee("NV01", "An", 8000000)
        engineer = SoftwareEngineer("KS01", "Nam", 15000000, "Python", 2000000)
        with ProjectTeam("DA01", "Dự án", employee) as team:
            team.addMember(engineer)
            self.assertEqual(team.calculateTotalMonthlyCost(), 25000000)

    def test_shared_employee_survives_close(self):
        employee = Employee("NV01", "An", 100)
        with ProjectTeam("DA01", "Một", employee) as first:
            with ProjectTeam("DA02", "Hai", employee) as second:
                self.assertIs(first.leader, second.leader)
            self.assertEqual(second.members, ())
            self.assertEqual(employee.baseSalary, 100)
            self.assertTrue(first.contains(employee.id))
            second.close()  # Đóng lần nữa không gây lỗi.
            with self.assertRaises(RuntimeError):
                second.addMember(employee)

    def test_invalid_project_and_member(self):
        with self.assertRaises(ValueError):
            ProjectTeam(" ", "Dự án")
        with self.assertRaises(ValueError):
            ProjectTeam("DA01", "")
        with ProjectTeam("DA01", "Dự án") as team:
            with self.assertRaises(TypeError):
                team.addMember(None)


if __name__ == "__main__":
    unittest.main()

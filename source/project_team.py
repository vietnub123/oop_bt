"""
/****************/
Mã sinh viên: 202419016
Họ tên: Phạm Xuân Việt
/****************/
"""

from employee import Employee


class ProjectTeam:
    """Quản lý thành viên; nhóm không chịu trách nhiệm hủy nhân sự."""

    def __init__(self, projectCode, projectName, leader=None):
        if not isinstance(projectCode, str) or not projectCode.strip():
            raise ValueError("Mã dự án không được rỗng.")
        if not isinstance(projectName, str) or not projectName.strip():
            raise ValueError("Tên dự án không được rỗng.")
        self._projectCode = projectCode.strip()
        self._projectName = projectName.strip()
        self._members = []
        self._leader = None
        self._closed = False
        if leader is not None:
            self.addMember(leader, True)

    @property
    def leader(self):
        return self._leader

    @property
    def members(self):
        # Trả về tuple để bên ngoài không tự thêm/xóa trong danh sách gốc.
        return tuple(self._members)

    def _checkOpen(self):
        if self._closed:
            raise RuntimeError("Nhóm đã đóng.")

    def contains(self, employeeId):
        self._checkOpen()
        return any(member.id == employeeId for member in self._members)

    def addMember(self, employee, makeLeader=False):
        self._checkOpen()
        if not isinstance(employee, Employee):
            raise TypeError("Thành viên phải là Employee hoặc SoftwareEngineer.")
        if self.contains(employee.id):
            return False
        self._members.append(employee)
        if makeLeader:
            self._leader = employee
        return True

    def removeMember(self, employeeId):
        self._checkOpen()
        if self._leader is not None and self._leader.id == employeeId:
            return False
        for member in self._members:
            if member.id == employeeId:
                self._members.remove(member)
                return True
        return False

    def changeLeader(self, employee):
        self._checkOpen()
        if not isinstance(employee, Employee):
            raise TypeError("Trưởng nhóm phải là một nhân sự.")
        for member in self._members:
            if member.id == employee.id:
                # Không thay thế âm thầm một đối tượng khác có cùng mã.
                if member is not employee:
                    return False
                self._leader = member
                return True
        self._members.append(employee)
        self._leader = employee
        return True

    def calculateTotalMonthlyCost(self):
        self._checkOpen()
        # Lời gọi này tự chọn phương thức của đúng lớp tại thời điểm chạy.
        return sum(member.calculateMonthlyCost() for member in self._members)

    def displayTeam(self):
        self._checkOpen()
        print(f"Dự án {self._projectCode}: {self._projectName}")
        leaderName = self._leader.fullName if self._leader else "Chưa có"
        print(f"Trưởng nhóm: {leaderName}")
        if not self._members:
            print("Chưa có thành viên.")
        for member in self._members:
            member.displayInfo()
        print(f"Tổng chi phí: {self.calculateTotalMonthlyCost():,.0f} đồng/tháng")

    def close(self):
        if not self._closed:
            # Chỉ bỏ tham chiếu của nhóm, không gọi hàm hủy của nhân sự.
            self._members.clear()
            self._leader = None
            self._closed = True
            print(f"Đóng ProjectTeam: {self._projectCode}")

    def __enter__(self):
        self._checkOpen()
        return self

    def __exit__(self, excType, excValue, traceback):
        self.close()
        return False

    def __del__(self):
        if hasattr(self, "_closed"):
            self.close()

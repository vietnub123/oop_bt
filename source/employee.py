"""
/****************/
Mã sinh viên: 202419016
Họ tên: Phạm Xuân Việt
/****************/
"""

import math


class Employee:
    """Lưu thông tin nhân sự và tính chi phí lương hằng tháng."""

    def __init__(self, id="UNKNOWN", fullName="Unnamed employee", baseSalary=0):
        if not isinstance(id, str) or not id.strip():
            raise ValueError("Mã nhân sự không được rỗng.")
        if not isinstance(fullName, str) or not fullName.strip():
            raise ValueError("Họ tên không được rỗng.")
        if not math.isfinite(baseSalary) or baseSalary < 0:
            raise ValueError("Lương phải là số hữu hạn, không âm.")
        self._id = id.strip()
        self._fullName = fullName.strip()
        self._baseSalary = baseSalary

    # Chỉ cho đọc mã qua property để tránh đổi mã gây trùng trong nhóm.
    @property
    def id(self):
        return self._id

    @property
    def fullName(self):
        return self._fullName

    @property
    def baseSalary(self):
        return self._baseSalary

    def increaseSalary(self, value, byPercentage=False):
        """Tham số mặc định thay cho hai phiên bản nạp chồng trong đề."""
        if not math.isfinite(value) or value <= 0:
            raise ValueError("Giá trị tăng phải là số hữu hạn, lớn hơn 0.")
        amount = self._baseSalary * (value / 100) if byPercentage else value
        newSalary = self._baseSalary + amount
        if not math.isfinite(newSalary):
            raise ValueError("Lương sau khi tăng vượt giới hạn số.")
        self._baseSalary = newSalary

    def calculateMonthlyCost(self):
        return self._baseSalary

    def displayInfo(self):
        print(f"{self.id} | {self.fullName} | Lương: {self.baseSalary:,.0f}")

    def __del__(self):
        # Constructor có thể lỗi trước khi gán thuộc tính.
        if hasattr(self, "_id"):
            print(f"Hủy Employee: {self.id}")

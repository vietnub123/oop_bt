"""
/****************/
Mã sinh viên: 202419016
Họ tên: Phạm Xuân Việt
/****************/
"""

import math
from employee import Employee


class SoftwareEngineer(Employee):
    """Kỹ sư có thêm ngôn ngữ chính và phụ cấp kỹ thuật."""

    def __init__(self, id, fullName, *args):
        # Hai cách gọi: (id, tên, ngôn ngữ) và (id, tên, lương, ngôn ngữ, phụ cấp).
        if len(args) == 1:
            baseSalary, primaryLanguage, technicalAllowance = 0, args[0], 0
        elif len(args) == 3:
            baseSalary, primaryLanguage, technicalAllowance = args
        else:
            raise TypeError("SoftwareEngineer cần 3 hoặc 5 đối số.")
        if not isinstance(primaryLanguage, str) or not primaryLanguage.strip():
            raise ValueError("Ngôn ngữ lập trình chính không được rỗng.")
        if not math.isfinite(technicalAllowance) or technicalAllowance < 0:
            raise ValueError("Phụ cấp phải là số hữu hạn, không âm.")
        super().__init__(id, fullName, baseSalary)
        self._primaryLanguage = primaryLanguage.strip()
        self._technicalAllowance = technicalAllowance

    @property
    def primaryLanguage(self):
        return self._primaryLanguage

    @property
    def technicalAllowance(self):
        return self._technicalAllowance

    def calculateMonthlyCost(self):
        return self.baseSalary + self.technicalAllowance

    def displayInfo(self):
        print(f"{self.id} | {self.fullName} | Lương: {self.baseSalary:,.0f}")
        print(f"  Ngôn ngữ: {self.primaryLanguage} | "
              f"Phụ cấp: {self.technicalAllowance:,.0f} | "
              f"Chi phí: {self.calculateMonthlyCost():,.0f}")

    def __del__(self):
        if hasattr(self, "_primaryLanguage"):
            print(f"Hủy SoftwareEngineer: {self.id}")
        super().__del__()

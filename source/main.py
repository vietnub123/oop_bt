"""
/****************/
Mã sinh viên: 202419016
Họ tên: Phạm Xuân Việt
/****************/
"""

from employee import Employee
from software_engineer import SoftwareEngineer
from project_team import ProjectTeam


def main():
    print("BÀI 03 - NHÓM DỰ ÁN VÀ NHÂN SỰ")
    print("Phạm Xuân Việt - 202419016")

    print("\n[1-2] Tạo nhân sự bằng các constructor khác nhau")
    nv1 = Employee("NV01", "Nguyễn Minh An")
    nv2 = Employee("NV02", "Trần Thu Hà", 10000000)
    ks1 = SoftwareEngineer("KS01", "Lê Hoàng Nam", "Python")
    ks2 = SoftwareEngineer("KS02", "Đỗ Mai Linh", 15000000, "C#", 2000000)
    for employee in (nv1, nv2, ks1, ks2):
        employee.displayInfo()

    print("\n[3-4] Tăng lương cố định và theo phần trăm")
    nv1.increaseSalary(8000000)
    nv2.increaseSalary(10, True)
    nv1.displayInfo()
    nv2.displayInfo()
    assert nv1.baseSalary == 8000000 and nv2.baseSalary == 11000000

    with ProjectTeam("DA01", "Quản lý thư viện") as team1:
        print("\n[5] Tạo nhóm chưa có trưởng nhóm")
        team1.displayTeam()
        print("\n[6] Thêm nhân viên:", team1.addMember(nv1))
        print("[7] Thêm kỹ sư làm trưởng nhóm:", team1.addMember(ks2, True))
        duplicate = team1.addMember(nv1)
        print("[8] Thêm lại NV01:", duplicate)
        assert not duplicate and len(team1.members) == 2

        print("\n[9-10] Hiển thị đa hình và tổng chi phí")
        team1.displayTeam()
        assert team1.calculateTotalMonthlyCost() == 25000000

        removed = team1.removeMember(ks2.id)
        print("\n[11] Xóa trưởng nhóm KS02:", removed)
        assert not removed
        print("[12] Đổi trưởng nhóm sang NV01:", team1.changeLeader(nv1))
        assert team1.contains(ks2.id)  # Người cũ vẫn ở trong nhóm.
        print("     Xóa trưởng nhóm cũ KS02:", team1.removeMember(ks2.id))
        assert team1.leader is nv1 and not team1.contains(ks2.id)

        print("\n[13] NV01 đồng thời thuộc hai dự án")
        with ProjectTeam("DA02", "Website câu lạc bộ", nv1) as team2:
            team2.addMember(nv2)
            team2.displayTeam()
            print("NV01 là cùng một đối tượng:", team1.leader is team2.leader)
            assert team1.leader is team2.leader
            print("[14] Kết thúc khối with của nhóm DA02")

        print("\n[15] NV01 vẫn tồn tại sau khi đóng DA02")
        nv1.displayInfo()
        print("NV01 vẫn thuộc DA01:", team1.contains(nv1.id))
        assert team1.contains(nv1.id) and nv1.baseSalary == 8000000

    print("\nHoàn thành 15 bước kiểm thử.")
    print("Kết thúc main, các nhân sự không còn được tham chiếu sẽ được thu hồi.")


if __name__ == "__main__":
    main()

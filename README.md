# Bài 03 - Nhóm dự án và nhân sự

- Họ tên: Phạm Xuân Việt
- MSSV: 202419016
- Ngôn ngữ: Python 3

## Chạy

Mở terminal trong thư mục `source`:

```bash
python main.py
python test_cases.py
```

Không cần cài thêm thư viện. Chương trình chính chạy 15 bước của đề;
file kiểm thử có 15 ca kiểm tra các ràng buộc và trường hợp biên.

## Các file

- `source/employee.py`: nhân sự thông thường.
- `source/software_engineer.py`: kỹ sư phần mềm, kế thừa Employee.
- `source/project_team.py`: danh sách thành viên và trưởng nhóm.
- `source/main.py`: chạy kịch bản của đề.
- `source/test_cases.py`: kiểm thử bằng unittest.
- `report/`: báo cáo Word và PDF.
- `evidence/`: sơ đồ lớp, hình ảnh và log chạy thực tế.

Python không hỗ trợ nạp chồng trực tiếp bằng nhiều định nghĩa cùng tên.
Bài dùng tham số mặc định và xử lý số đối số tương ứng với các cách gọi của đề.
`with` gọi `close()` khi ra khỏi khối lệnh; việc này bỏ tham chiếu của nhóm,
không chủ động hủy các Employee. `__del__` chỉ dùng để quan sát lúc thu hồi.



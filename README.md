# Python Student Management System

Ứng dụng quản lý sinh viên chạy trên terminal, được viết bằng Python. Chương
trình hỗ trợ các thao tác CRUD, tìm kiếm, xếp loại theo GPA và tự động lưu dữ
liệu vào file JSON.

## Chức năng

- Thêm sinh viên mới.
- Hiển thị danh sách sinh viên.
- Tìm sinh viên theo ID.
- Tìm kiếm gần đúng theo tên, không phân biệt chữ hoa và chữ thường.
- Cập nhật thông tin sinh viên.
- Xóa sinh viên.
- Sắp xếp sinh viên theo GPA từ cao xuống thấp.
- Tính GPA từ điểm Toán và Lập trình.
- Xếp loại học lực tự động.
- Tự động đọc và lưu dữ liệu bằng JSON.

## Quy tắc dữ liệu

| Trường | Quy tắc |
| --- | --- |
| Student ID | Không được để trống và không được trùng |
| Name | Có ít nhất 2 ký tự sau khi loại bỏ khoảng trắng thừa |
| Age | Là số nguyên từ 16 đến 100 |
| Math score | Là số hữu hạn từ 0 đến 10 |
| Programming score | Là số hữu hạn từ 0 đến 10 |

Giá trị đặc biệt như `NaN`, vô cực, chuỗi rỗng hoặc dữ liệu sai kiểu đều bị từ
chối.

## Cách tính GPA và xếp loại

```text
GPA = (Math score + Programming score) / 2
```

| GPA | Classification |
| --- | --- |
| Từ 8.5 trở lên | Excellent |
| Từ 7.0 đến dưới 8.5 | Good |
| Từ 5.5 đến dưới 7.0 | Average |
| Dưới 5.5 | Weak |

## Cấu trúc project

```text
Python Student Management System/
├── data/
│   └── students.json
├── models/
│   ├── __init__.py
│   └── student.py
├── repositories/
│   ├── __init__.py
│   └── student_repository.py
├── services/
│   ├── __init__.py
│   └── student_service.py
├── tests/
│   ├── test_student.py
│   ├── test_student_repository.py
│   ├── test_student_service.py
│   └── test_validator.py
├── utils/
│   ├── __init__.py
│   └── validator.py
├── main.py
├── student_app.py
├── requirements.txt
└── README.md
```

Vai trò của từng phần:

| Thành phần | Trách nhiệm |
| --- | --- |
| `main.py` | Điểm khởi động của chương trình |
| `student_app.py` | Hiển thị menu và xử lý nhập/xuất trên terminal |
| `models/student.py` | Định nghĩa đối tượng `Student`, GPA, xếp loại và validation |
| `services/student_service.py` | Xử lý nghiệp vụ thêm, tìm, sửa, xóa và sắp xếp |
| `repositories/student_repository.py` | Đọc và ghi danh sách sinh viên bằng JSON |
| `utils/validator.py` | Chứa các quy tắc kiểm tra dữ liệu dùng bởi model |
| `tests/` | Chứa các automated test của project |

## Yêu cầu

- Python 3.8 trở lên.
- Không cần cài thư viện bên ngoài; project chỉ sử dụng Python Standard Library.

Kiểm tra phiên bản Python bằng lệnh:

```powershell
python --version
```

## Chạy chương trình

Mở terminal tại thư mục gốc của project và chạy:

```powershell
python main.py
```

Menu chính:

```text
========== STUDENT MANAGEMENT ==========
1. Add Student
2. View Students
3. Find Student by ID
4. Search Student by Name
5. Update Student
6. Delete Student
7. Sort Students by GPA
0. Exit
```

Khi cập nhật sinh viên, nhấn `Enter` mà không nhập giá trị để giữ lại dữ liệu
hiện tại.

## Lưu trữ dữ liệu

Dữ liệu được đọc từ `data/students.json` khi chương trình khởi động và được lưu
tự động sau mỗi thao tác thêm, cập nhật hoặc xóa.

Ví dụ:

```json
[
    {
        "student_id": "SV001",
        "name": "Nguyễn Văn An",
        "age": 20,
        "math_score": 8.0,
        "programming_score": 9.0
    }
]
```

Nếu file chưa tồn tại, chương trình sẽ bắt đầu với danh sách rỗng. File JSON
phải chứa một danh sách và mỗi phần tử phải có đủ năm trường như ví dụ trên.

## Chạy automated test

Chạy toàn bộ test bằng lệnh:

```powershell
python -m unittest discover -s tests -v
```

Bộ test hiện kiểm tra:

- Tính GPA và các mốc xếp loại.
- Chuyển đổi `Student` sang dictionary và ngược lại.
- Validation tuổi, tên, ID và điểm số.
- Chặn điểm `NaN`, vô cực và giá trị ngoài phạm vi.
- Thêm, tìm, cập nhật, xóa và sắp xếp sinh viên.
- Chặn Student ID trùng.
- Tìm kiếm tên rỗng và tìm kiếm không phân biệt hoa/thường.
- Đọc, ghi Unicode và phát hiện JSON sai định dạng.

Các test lưu trữ sử dụng thư mục tạm, vì vậy không thay đổi file
`data/students.json` thật.

Kết quả thành công có dạng:

```text
Ran 28 tests

OK
```

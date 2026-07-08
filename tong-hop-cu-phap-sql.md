# Tổng Hợp Cú Pháp SQL Cơ Bản — Tài Liệu Ôn Tập

> Dùng ví dụ với bảng mẫu:
> - `SinhVien(MaSV, HoTen, NgaySinh, GioiTinh, MaLop, DiemTB)`
> - `Lop(MaLop, TenLop, SiSo)`
> - `KhoaHoc(MaKH, TenKH, SoTinChi)`
> - `DangKy(MaSV, MaKH, DiemThi)`

---

## 1. SELECT — Truy vấn cơ bản

```sql
-- Lấy tất cả cột, tất cả dòng
SELECT * FROM SinhVien;

-- Lấy một số cột cụ thể
SELECT MaSV, HoTen, DiemTB FROM SinhVien;

-- Đặt bí danh (alias) cho cột
SELECT HoTen AS "Họ Tên", DiemTB AS DiemTrungBinh FROM SinhVien;

-- Loại bỏ dòng trùng lặp
SELECT DISTINCT MaLop FROM SinhVien;
```

**Ghi nhớ:** `AS` có thể bỏ, chỉ cần `HoTen "Họ Tên"` cũng được (tùy hệ CSDL).

---

## 2. WHERE — Lọc điều kiện

```sql
-- So sánh cơ bản: =, <>, >, <, >=, <=
SELECT * FROM SinhVien WHERE DiemTB >= 8;

-- Nhiều điều kiện: AND, OR, NOT
SELECT * FROM SinhVien WHERE DiemTB >= 8 AND GioiTinh = 'Nam';
SELECT * FROM SinhVien WHERE MaLop = 'D20CQCC01' OR MaLop = 'D20CQCC02';
SELECT * FROM SinhVien WHERE NOT GioiTinh = 'Nam';

-- BETWEEN: trong khoảng (bao gồm 2 đầu mút)
SELECT * FROM SinhVien WHERE DiemTB BETWEEN 5 AND 7;

-- IN: thuộc một danh sách
SELECT * FROM SinhVien WHERE MaLop IN ('D20CQCC01', 'D20CQCC02');

-- LIKE: tìm theo mẫu chuỗi
-- % : bất kỳ chuỗi ký tự nào (kể cả rỗng)
-- _ : đúng một ký tự bất kỳ
SELECT * FROM SinhVien WHERE HoTen LIKE 'Nguyễn%';   -- bắt đầu bằng "Nguyễn"
SELECT * FROM SinhVien WHERE HoTen LIKE '%Anh';       -- kết thúc bằng "Anh"
SELECT * FROM SinhVien WHERE HoTen LIKE '%Văn%';      -- chứa "Văn"
SELECT * FROM SinhVien WHERE MaSV LIKE 'B25_CC%';     -- ký tự thứ 4 bất kỳ

-- IS NULL / IS NOT NULL: kiểm tra giá trị rỗng
SELECT * FROM SinhVien WHERE DiemTB IS NULL;
SELECT * FROM SinhVien WHERE DiemTB IS NOT NULL;
```

**Lỗi hay gặp:** dùng `= NULL` thay vì `IS NULL` → luôn sai, vì NULL không so sánh bằng được.

---

## 3. ORDER BY — Sắp xếp

```sql
-- Tăng dần (mặc định là ASC, không ghi cũng được)
SELECT * FROM SinhVien ORDER BY DiemTB ASC;

-- Giảm dần
SELECT * FROM SinhVien ORDER BY DiemTB DESC;

-- Sắp xếp theo nhiều cột (ưu tiên từ trái sang phải)
SELECT * FROM SinhVien ORDER BY MaLop ASC, DiemTB DESC;
```

---

## 4. Hàm tổng hợp (Aggregate Functions)

```sql
SELECT COUNT(*) FROM SinhVien;              -- đếm số dòng
SELECT COUNT(DiemTB) FROM SinhVien;         -- đếm số dòng KHÔNG null ở cột đó
SELECT SUM(SoTinChi) FROM KhoaHoc;          -- tổng
SELECT AVG(DiemTB) FROM SinhVien;           -- trung bình
SELECT MAX(DiemTB) FROM SinhVien;           -- lớn nhất
SELECT MIN(DiemTB) FROM SinhVien;           -- nhỏ nhất
```

---

## 5. GROUP BY và HAVING — Gom nhóm

```sql
-- Đếm số sinh viên theo từng lớp
SELECT MaLop, COUNT(*) AS SoLuong
FROM SinhVien
GROUP BY MaLop;

-- Điểm trung bình của mỗi lớp
SELECT MaLop, AVG(DiemTB) AS DiemTB_Lop
FROM SinhVien
GROUP BY MaLop;

-- HAVING: lọc SAU KHI gom nhóm (WHERE không lọc được hàm tổng hợp)
SELECT MaLop, AVG(DiemTB) AS DiemTB_Lop
FROM SinhVien
GROUP BY MaLop
HAVING AVG(DiemTB) >= 7;
```

**Ghi nhớ cực quan trọng — thứ tự tư duy khi viết câu SQL:**
```
SELECT ... 
FROM ...
WHERE ...        -- lọc TỪNG DÒNG trước khi gom nhóm
GROUP BY ...
HAVING ...        -- lọc SAU KHI gom nhóm (dùng được hàm tổng hợp)
ORDER BY ...
```
- `WHERE` không dùng được `COUNT()`, `AVG()`,... → phải dùng `HAVING`.
- Thứ tự viết: `SELECT → FROM → WHERE → GROUP BY → HAVING → ORDER BY`
- Thứ tự CSDL thực thi: `FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY`

---

## 6. JOIN — Nối bảng

Đây là phần hay gặp lỗi nhất, tập trung kỹ.

### 6.1 INNER JOIN — chỉ lấy dòng khớp ở cả 2 bảng

```sql
SELECT SV.HoTen, L.TenLop
FROM SinhVien SV
INNER JOIN Lop L ON SV.MaLop = L.MaLop;
```

### 6.2 LEFT JOIN — lấy hết bảng trái, bảng phải không khớp thì NULL

```sql
-- Lấy tất cả sinh viên, kể cả sinh viên chưa đăng ký khóa học nào
SELECT SV.HoTen, DK.MaKH
FROM SinhVien SV
LEFT JOIN DangKy DK ON SV.MaSV = DK.MaSV;
```

### 6.3 RIGHT JOIN — ngược lại LEFT JOIN

```sql
SELECT SV.HoTen, DK.MaKH
FROM SinhVien SV
RIGHT JOIN DangKy DK ON SV.MaSV = DK.MaSV;
```

### 6.4 FULL OUTER JOIN — lấy hết cả 2 bên (MySQL không hỗ trợ trực tiếp)

```sql
SELECT SV.HoTen, DK.MaKH
FROM SinhVien SV
FULL OUTER JOIN DangKy DK ON SV.MaSV = DK.MaSV;
```

### 6.5 Nối nhiều bảng cùng lúc

```sql
SELECT SV.HoTen, KH.TenKH, DK.DiemThi
FROM SinhVien SV
JOIN DangKy DK ON SV.MaSV = DK.MaSV
JOIN KhoaHoc KH ON DK.MaKH = KH.MaKH
WHERE DK.DiemThi >= 5;
```

### 6.6 Cách nhớ nhanh khác biệt các JOIN

| Loại JOIN | Lấy gì |
|---|---|
| INNER JOIN | Chỉ dòng khớp cả 2 bảng |
| LEFT JOIN | Hết bảng trái + phần khớp bảng phải |
| RIGHT JOIN | Hết bảng phải + phần khớp bảng trái |
| FULL JOIN | Hết cả 2 bảng, không khớp thì NULL |

---

## 7. Toán tử tập hợp (UNION, INTERSECT, EXCEPT)

Yêu cầu: các câu SELECT phải có **cùng số cột** và **kiểu dữ liệu tương ứng**.

```sql
-- UNION: gộp, tự động loại trùng
SELECT MaSV FROM DangKy WHERE MaKH = 'KH01'
UNION
SELECT MaSV FROM DangKy WHERE MaKH = 'KH02';

-- UNION ALL: gộp, GIỮ trùng (nhanh hơn UNION)
SELECT MaSV FROM DangKy WHERE MaKH = 'KH01'
UNION ALL
SELECT MaSV FROM DangKy WHERE MaKH = 'KH02';

-- INTERSECT: giao (dòng có ở cả 2 truy vấn)
SELECT MaSV FROM DangKy WHERE MaKH = 'KH01'
INTERSECT
SELECT MaSV FROM DangKy WHERE MaKH = 'KH02';

-- EXCEPT (MySQL dùng khác - xem phần Subquery bên dưới thay thế)
SELECT MaSV FROM DangKy WHERE MaKH = 'KH01'
EXCEPT
SELECT MaSV FROM DangKy WHERE MaKH = 'KH02';
```

---

## 8. Truy vấn con (Subquery)

```sql
-- Subquery trong WHERE
SELECT HoTen FROM SinhVien
WHERE DiemTB > (SELECT AVG(DiemTB) FROM SinhVien);

-- Subquery với IN
SELECT HoTen FROM SinhVien
WHERE MaSV IN (SELECT MaSV FROM DangKy WHERE MaKH = 'KH01');

-- Subquery với NOT IN (thay thế EXCEPT trong MySQL)
SELECT MaSV FROM SinhVien
WHERE MaSV NOT IN (SELECT MaSV FROM DangKy WHERE MaKH = 'KH01');

-- Subquery với EXISTS (kiểm tra tồn tại)
SELECT HoTen FROM SinhVien SV
WHERE EXISTS (SELECT 1 FROM DangKy DK WHERE DK.MaSV = SV.MaSV);

-- Subquery trong FROM (bảng tạm)
SELECT MaLop, DiemTB_Max
FROM (
    SELECT MaLop, MAX(DiemTB) AS DiemTB_Max
    FROM SinhVien
    GROUP BY MaLop
) AS Tmp;
```

---

## 9. Thao tác dữ liệu: INSERT, UPDATE, DELETE

```sql
-- INSERT: thêm dòng mới
INSERT INTO SinhVien (MaSV, HoTen, NgaySinh, GioiTinh, MaLop, DiemTB)
VALUES ('B25DCCC999', 'Trần Văn A', '2006-05-10', 'Nam', 'D25CQCC01', NULL);

-- Thêm nhiều dòng cùng lúc
INSERT INTO SinhVien (MaSV, HoTen)
VALUES 
  ('SV01', 'Nguyễn A'),
  ('SV02', 'Trần B');

-- UPDATE: sửa dữ liệu — LUÔN có WHERE, không sẽ sửa TOÀN BỘ bảng!
UPDATE SinhVien
SET DiemTB = 8.5
WHERE MaSV = 'B25DCCC999';

-- DELETE: xóa dòng — LUÔN có WHERE, không sẽ xóa TOÀN BỘ bảng!
DELETE FROM SinhVien
WHERE MaSV = 'B25DCCC999';
```

---

## 10. Định nghĩa cấu trúc: CREATE, ALTER, DROP

```sql
-- Tạo bảng
CREATE TABLE SinhVien (
    MaSV VARCHAR(10) PRIMARY KEY,
    HoTen NVARCHAR(50) NOT NULL,
    NgaySinh DATE,
    GioiTinh VARCHAR(3),
    MaLop VARCHAR(10),
    DiemTB FLOAT,
    FOREIGN KEY (MaLop) REFERENCES Lop(MaLop)
);

-- Thêm cột
ALTER TABLE SinhVien ADD Email VARCHAR(50);

-- Sửa kiểu dữ liệu cột
ALTER TABLE SinhVien MODIFY DiemTB DECIMAL(3,1);

-- Xóa cột
ALTER TABLE SinhVien DROP COLUMN Email;

-- Xóa toàn bộ bảng (cả cấu trúc)
DROP TABLE SinhVien;

-- Xóa hết dữ liệu, giữ cấu trúc (nhanh hơn DELETE)
TRUNCATE TABLE SinhVien;
```

---

## 11. Ràng buộc thường gặp (Constraints)

```sql
CREATE TABLE KhoaHoc (
    MaKH VARCHAR(10) PRIMARY KEY,          -- khóa chính
    TenKH NVARCHAR(50) NOT NULL,           -- không được rỗng
    SoTinChi INT DEFAULT 3,                -- giá trị mặc định
    UNIQUE (TenKH),                        -- không trùng
    CHECK (SoTinChi > 0)                   -- điều kiện kiểm tra
);
```

| Ràng buộc | Ý nghĩa |
|---|---|
| `PRIMARY KEY` | Khóa chính, không trùng, không NULL |
| `FOREIGN KEY` | Khóa ngoại, tham chiếu bảng khác |
| `NOT NULL` | Không được để trống |
| `UNIQUE` | Giá trị không trùng lặp |
| `DEFAULT` | Giá trị mặc định khi không nhập |
| `CHECK` | Điều kiện phải thỏa mãn |

---

## 12. Hàm xử lý chuỗi, ngày tháng thường dùng

```sql
-- Chuỗi
SELECT UPPER(HoTen) FROM SinhVien;          -- viết hoa
SELECT LOWER(HoTen) FROM SinhVien;          -- viết thường
SELECT LENGTH(HoTen) FROM SinhVien;         -- độ dài chuỗi
SELECT CONCAT(HoTen, ' - ', MaLop) FROM SinhVien;  -- nối chuỗi
SELECT SUBSTRING(HoTen, 1, 3) FROM SinhVien; -- cắt chuỗi (từ vị trí 1, lấy 3 ký tự)
SELECT TRIM(HoTen) FROM SinhVien;           -- xóa khoảng trắng 2 đầu

-- Ngày tháng
SELECT NOW();                                -- ngày giờ hiện tại
SELECT CURDATE();                            -- ngày hiện tại
SELECT YEAR(NgaySinh) FROM SinhVien;        -- lấy năm
SELECT DATEDIFF(NOW(), NgaySinh) FROM SinhVien; -- khoảng cách ngày

-- Xử lý NULL
SELECT COALESCE(DiemTB, 0) FROM SinhVien;   -- nếu NULL thì thay bằng 0
```

---

## 13. LIMIT / OFFSET — Giới hạn số dòng kết quả

```sql
-- Lấy 5 sinh viên điểm cao nhất
SELECT * FROM SinhVien ORDER BY DiemTB DESC LIMIT 5;

-- Phân trang: bỏ qua 10 dòng đầu, lấy 5 dòng tiếp theo
SELECT * FROM SinhVien ORDER BY MaSV LIMIT 5 OFFSET 10;
```

---

## 14. CASE WHEN — Điều kiện trong SELECT

```sql
SELECT HoTen, DiemTB,
    CASE
        WHEN DiemTB >= 8 THEN 'Giỏi'
        WHEN DiemTB >= 6.5 THEN 'Khá'
        WHEN DiemTB >= 5 THEN 'Trung bình'
        ELSE 'Yếu'
    END AS XepLoai
FROM SinhVien;
```

---

## 15. Tổng kết thứ tự viết một câu SELECT đầy đủ

```sql
SELECT [DISTINCT] cột1, cột2, hàm_tổng_hợp(...)
FROM bảng1
[INNER/LEFT/RIGHT JOIN bảng2 ON điều_kiện]
[WHERE điều_kiện_lọc_dòng]
[GROUP BY cột]
[HAVING điều_kiện_lọc_nhóm]
[ORDER BY cột [ASC|DESC]]
[LIMIT n [OFFSET m]];
```

**Mẹo làm bài tập:** đọc đề, xác định lần lượt:
1. Cần bảng nào → `FROM`, có nối bảng không → `JOIN`
2. Cần lọc điều kiện gì trên từng dòng → `WHERE`
3. Có cần gom nhóm/thống kê không (đếm, tổng, trung bình theo...) → `GROUP BY`
4. Có lọc trên kết quả gom nhóm không (VD: "những lớp có điểm TB > 7") → `HAVING`
5. Cần sắp xếp không → `ORDER BY`
6. Cần giới hạn số dòng không → `LIMIT`

---

*Chun có thể lưu file này lại để ôn thi hoặc làm bài tập thực hành. Nếu có bài tập cụ thể, cứ gửi đề bài, mình sẽ hướng dẫn từng bước theo đúng quy trình tư duy ở mục 15.*

// mockData.js - Dữ liệu giả, sẽ thay bằng API thật khi làm Backend

const mockBooks = [
    {
        id: 1,
        tenSach: "Lập trình hướng đối tượng với Java",
        tacGia: "Nguyễn Văn Hòa",
        theLoai: "Công nghệ thông tin",
        namXuatBan: 2022,
        soLuong: 10,
        soLuongCon: 4,
        trangThai: "con_hang" // con_hang | het_hang
    },
    {
        id: 2,
        tenSach: "Cấu trúc dữ liệu và giải thuật",
        tacGia: "Đinh Mạnh Tường",
        theLoai: "Công nghệ thông tin",
        namXuatBan: 2020,
        soLuong: 8,
        soLuongCon: 0,
        trangThai: "het_hang"
    },
    {
        id: 3,
        tenSach: "Cơ sở dữ liệu SQL căn bản",
        tacGia: "Trần Thị Thanh Hải",
        theLoai: "Công nghệ thông tin",
        namXuatBan: 2023,
        soLuong: 15,
        soLuongCon: 9,
        trangThai: "con_hang"
    },
    {
        id: 4,
        tenSach: "Toán rời rạc ứng dụng trong Tin học",
        tacGia: "Kenneth Rosen",
        theLoai: "Toán học",
        namXuatBan: 2019,
        soLuong: 6,
        soLuongCon: 2,
        trangThai: "con_hang"
    },
    {
        id: 5,
        tenSach: "Mạng máy tính",
        tacGia: "Andrew S. Tanenbaum",
        theLoai: "Mạng máy tính",
        namXuatBan: 2021,
        soLuong: 5,
        soLuongCon: 5,
        trangThai: "con_hang"
    }
];

const mockReaders = [
    {
        id: 1,
        hoTen: "Nguyễn Văn A",
        email: "vana@gmail.com",
        soDienThoai: "0987654321",
        lop: "D22CQCN01",
        ngayDangKy: "2026-01-15",
        trangThai: "hoat_dong" // hoat_dong | bi_khoa
    },
    {
        id: 2,
        hoTen: "Trần Thị B",
        email: "tranb@gmail.com",
        soDienThoai: "0912345678",
        lop: "D22CQCN02",
        ngayDangKy: "2026-02-20",
        trangThai: "hoat_dong"
    },
    {
        id: 3,
        hoTen: "Lê Văn C",
        email: "levanc@gmail.com",
        soDienThoai: "0977123456",
        lop: "D22CQCN01",
        ngayDangKy: "2026-03-05",
        trangThai: "bi_khoa"
    }
];

const mockBorrows = [
    {
        id: 1,
        maPhieu: "PM0001",
        bookId: 1,
        readerId: 1,
        ngayMuon: "2026-07-01",
        hanTra: "2026-07-15",
        ngayTraThucTe: null,
        trangThai: "dang_muon" // dang_muon | qua_han | da_tra
    },
    {
        id: 2,
        maPhieu: "PM0002",
        bookId: 2,
        readerId: 2,
        ngayMuon: "2026-06-20",
        hanTra: "2026-07-04",
        ngayTraThucTe: null,
        trangThai: "qua_han"
    },
    {
        id: 3,
        maPhieu: "PM0003",
        bookId: 3,
        readerId: 1,
        ngayMuon: "2026-06-10",
        hanTra: "2026-06-24",
        ngayTraThucTe: "2026-06-22",
        trangThai: "da_tra"
    }
];
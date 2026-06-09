// ===== DỮ LIỆU =====
let danhSachSach = [];
let idTiepTheo = 1; // đánh số thứ tự tự động

// ===== HÀM 1: Thêm sách =====
function themSach() {
  // Bước 1: Lấy giá trị từ các ô input
  let ten     = document.getElementById("inputTen").value.trim();
  let tacGia  = document.getElementById("inputTacGia").value.trim();
  let theLoai = document.getElementById("inputTheLoai").value.trim();
  let nam     = document.getElementById("inputNam").value.trim();

  // Bước 2: Kiểm tra ô trống (if/else)
  if (ten === "" || tacGia === "" || theLoai === "" || nam === "") {
    hienThongBao("Vui lòng điền đầy đủ thông tin!", "loi");
    return; // dừng hàm, không làm gì thêm
  }

  // Bước 3: Tạo object sách mới
  let sachMoi = {
    id: idTiepTheo,
    ten: ten,
    tacGia: tacGia,
    theLoai: theLoai,
    nam: nam
  };

  // Bước 4: Thêm vào mảng
  danhSachSach.push(sachMoi);
  idTiepTheo++;

  // Bước 5: Cập nhật giao diện
  hienThiDanhSach(danhSachSach);
  capNhatThongKe();
  xoaForm();
  hienThongBao("Thêm sách thành công!", "ok");
}

// ===== HÀM 2: Hiển thị danh sách ra bảng =====
function hienThiDanhSach(mangSach) {
  let bang = document.getElementById("bangSach");

  // Nếu không có sách nào
  if (mangSach.length === 0) {
    bang.innerHTML = `<tr><td colspan="6" class="empty">Chưa có sách nào!</td></tr>`;
    return;
  }

  // Dùng vòng lặp tạo từng hàng <tr>
  let html = "";
  for (let i = 0; i < mangSach.length; i++) {
    let s = mangSach[i];
    html += `
        <tr>
          <td style="color:#a89070">${i + 1}</td>
          <td style="font-weight:500">${s.ten}</td>
          <td>${s.tacGia}</td>
          <td><span class="badge">${s.theLoai}</span></td>
          <td>${s.nam}</td>
          <td>
            ${s.trangThai === "san-sang"
              ? `<span class="badge-san-sang">✅ Sẵn sàng</span>`
              : `<span class="badge-dang-muon">📖 Đang mượn<br>
                <small style="font-size:10px; color:#a89070">
                  ${s.nguoiMuon} · ${s.ngayMuon}
                </small></span>`
            }
          </td>
          <td style="display:flex; gap:6px; align-items:center;">
            ${s.trangThai === "san-sang"
              ? `<button class="btn-xoa" style="color:#2e7d32;"
                        onclick="moModalMuon(${s.id})">📖 Mượn</button>`
              : `<button class="btn-xoa" style="color:#1565c0;"
                        onclick="traSach(${s.id})">↩ Trả</button>`
            }
            <button class="btn-xoa" onclick="xoaSach(${s.id})">🗑 Xóa</button>
          </td>
        </tr>`;
  }
  bang.innerHTML = html;
}

// ===== HÀM 3: Xóa form sau khi thêm =====
function xoaForm() {
  document.getElementById("inputTen").value    = "";
  document.getElementById("inputTacGia").value = "";
  document.getElementById("inputTheLoai").value = "";
  document.getElementById("inputNam").value    = "";
}

// ===== HÀM 4: Hiện thông báo =====
function hienThongBao(noiDung, loai) {
  let hop = document.getElementById("thongBao");
  hop.innerText = noiDung;
  hop.style.display = "block";
  hop.className = loai === "loi" ? "tb-loi" : "tb-ok";

  // Tự ẩn sau 3 giây
  setTimeout(() => { hop.style.display = "none"; }, 3000);
}

// ===== HÀM 5: Cập nhật thống kê =====
function capNhatThongKe() {
  document.getElementById("tongSach").innerText = danhSachSach.length;

  // Đếm số thể loại không trùng nhau
  let cacTheLoai = [];
  for (let i = 0; i < danhSachSach.length; i++) {
    if (!cacTheLoai.includes(danhSachSach[i].theLoai)) {
      cacTheLoai.push(danhSachSach[i].theLoai);
    }
  }
  document.getElementById("tongTheLoai").innerText = cacTheLoai.length;
}

// ===== GẮN SỰ KIỆN =====
document.getElementById("btnThem").addEventListener("click", themSach);
// ===========================
// DỮ LIỆU
// ===========================


// ===========================
// HÀM 1: Thêm sách
// ===========================
function themSach() {
  // Bước 1: Lấy giá trị từ input
  let ten     = document.getElementById("inputTen").value.trim();
  let tacGia  = document.getElementById("inputTacGia").value.trim();
  let theLoai = document.getElementById("inputTheLoai").value.trim();
  let nam     = document.getElementById("inputNam").value.trim();

  // Bước 2: Kiểm tra ô trống (if/else ✅)
  if (ten === "" || tacGia === "" || theLoai === "" || nam === "") {
    hienThongBao("Vui lòng điền đầy đủ thông tin!", "loi");
    return; // dừng hàm tại đây
  }

  // Bước 3: Tạo object sách mới
  let sachMoi = {
    id: idTiepTheo,
    ten: ten,
    tacGia: tacGia,
    theLoai: theLoai,
    nam: nam,
    trangThai: "san-sang",
    nguoiMuon: "",
    ngayMuon: ""      
  };

  // Bước 4: Thêm vào mảng + tăng id
  danhSachSach.push(sachMoi);
  idTiepTheo++;

  // Bước 5: Cập nhật giao diện
  hienThiDanhSach(danhSachSach);
  capNhatThongKe();
  xoaForm();
  hienThongBao("Thêm sách thành công! 🎉", "ok");
}


// ===========================
// HÀM 2: Hiển thị danh sách
// ===========================
function hienThiDanhSach(mangSach) {
  let bang = document.getElementById("bangSach");

  // Nếu mảng rỗng
  if (mangSach.length === 0) {
    bang.innerHTML = `
      <tr>
        <td colspan="6" class="empty">Chưa có sách nào. Hãy thêm sách mới!</td>
      </tr>`;
    return;
  }

  // Vòng lặp tạo từng hàng <tr> (vòng lặp ✅)
  let html = "";
  for (let i = 0; i < mangSach.length; i++) {
    let s = mangSach[i];
    html += `
      <tr>
        <td style="color:#a89070">${i + 1}</td>
        <td style="font-weight:500">${s.ten}</td>
        <td>${s.tacGia}</td>
        <td><span class="badge">${s.theLoai}</span></td>
        <td>${s.nam}</td>
        <td>
          <button class="btn-xoa" onclick="xoaSach(${s.id})">🗑 Xóa</button>
        </td>
      </tr>`;
  }
  bang.innerHTML = html;
}


// ===========================
// HÀM 3: Xóa sách
// ===========================
function xoaSach(id) {
  // filter giữ lại những sách KHÔNG có id này
  danhSachSach = danhSachSach.filter(function(sach) {
    return sach.id !== id;
  });

  hienThiDanhSach(danhSachSach);
  capNhatThongKe();
  hienThongBao("Đã xóa sách.", "ok");
}


// ===========================
// HÀM 4: Tìm kiếm
// ===========================
function timKiem() {
  let tuKhoa = document.getElementById("inputTimKiem").value.trim().toLowerCase();

  // Nếu ô tìm kiếm trống → hiện lại toàn bộ
  if (tuKhoa === "") {
    hienThiDanhSach(danhSachSach);
    return;
  }

  // Lọc những sách có tên hoặc tác giả chứa từ khoá
  let ketQua = [];
  for (let i = 0; i < danhSachSach.length; i++) {
    let ten    = danhSachSach[i].ten.toLowerCase();
    let tacGia = danhSachSach[i].tacGia.toLowerCase();

    if (ten.includes(tuKhoa) || tacGia.includes(tuKhoa)) {
      ketQua.push(danhSachSach[i]);
    }
  }

  hienThiDanhSach(ketQua);
}


// ===========================
// HÀM 5: Cập nhật thống kê
// ===========================
function capNhatThongKe() {
  // Tổng số sách
  document.getElementById("tongSach").innerText = danhSachSach.length;

  // Đếm thể loại không trùng (vòng lặp ✅)
  let cacTheLoai = [];
  for (let i = 0; i < danhSachSach.length; i++) {
    if (!cacTheLoai.includes(danhSachSach[i].theLoai)) {
      cacTheLoai.push(danhSachSach[i].theLoai);
    }
  }
  document.getElementById("tongTheLoai").innerText = cacTheLoai.length;
}


// ===========================
// HÀM 6: Xoá form sau khi thêm
// ===========================
function xoaForm() {
  document.getElementById("inputTen").value     = "";
  document.getElementById("inputTacGia").value  = "";
  document.getElementById("inputTheLoai").value = "";
  document.getElementById("inputNam").value     = "";
}


// ===========================
// HÀM 7: Hiện thông báo
// ===========================
function hienThongBao(noiDung, loai) {
  let hop = document.getElementById("thongBao");
  hop.innerText    = noiDung;
  hop.style.display = "block";
  hop.className    = (loai === "loi") ? "tb-loi" : "tb-ok";

  // Tự ẩn sau 3 giây
  setTimeout(function() {
    hop.style.display = "none";
  }, 3000);
}

// ===========================
// HÀM 8: Mở modal mượn sách
// ===========================
let idDangMuon = null; // lưu id sách đang chờ xác nhận

function moModalMuon(id) {
  idDangMuon = id;

  // Điền ngày hôm nay tự động
  let homNay = new Date().toISOString().split("T")[0];
  document.getElementById("inputNgayMuon").value = homNay;
  document.getElementById("inputNguoiMuon").value = "";

  // Hiện modal
  let modal = document.getElementById("modalMuon");
  modal.style.display = "flex";
}


// ===========================
// HÀM 9: Xác nhận mượn sách
// ===========================
function xacNhanMuon() {
  let nguoiMuon = document.getElementById("inputNguoiMuon").value.trim();
  let ngayMuon  = document.getElementById("inputNgayMuon").value;

  if (nguoiMuon === "" || ngayMuon === "") {
    alert("Vui lòng điền tên người mượn và ngày mượn!");
    return;
  }

  // Tìm sách theo id và cập nhật trạng thái
  for (let i = 0; i < danhSachSach.length; i++) {
    if (danhSachSach[i].id === idDangMuon) {
      danhSachSach[i].trangThai = "dang-muon";
      danhSachSach[i].nguoiMuon = nguoiMuon;
      danhSachSach[i].ngayMuon  = ngayMuon;
      break;
    }
  }

  dongModal();
  hienThiDanhSach(danhSachSach);
  capNhatThongKe();
  hienThongBao(`Đã ghi nhận "${nguoiMuon}" mượn sách!`, "ok");
}


// ===========================
// HÀM 10: Trả sách
// ===========================
function traSach(id) {
  for (let i = 0; i < danhSachSach.length; i++) {
    if (danhSachSach[i].id === id) {
      danhSachSach[i].trangThai = "san-sang";
      danhSachSach[i].nguoiMuon = "";
      danhSachSach[i].ngayMuon  = "";
      break;
    }
  }

  hienThiDanhSach(danhSachSach);
  capNhatThongKe();
  hienThongBao("Đã trả sách thành công!", "ok");
}


// ===========================
// HÀM 11: Đóng modal
// ===========================
function dongModal() {
  document.getElementById("modalMuon").style.display = "none";
  idDangMuon = null;
}
// ===========================
// GẮN SỰ KIỆN
// ===========================
document.getElementById("btnThem").addEventListener("click", themSach);
document.getElementById("inputTimKiem").addEventListener("input", timKiem);
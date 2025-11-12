# ==============================
# CHƯƠNG TRÌNH TỪ ĐIỂN ANH - VIỆT
# ==============================

def menu():
    print("===== TỪ ĐIỂN ANH - VIỆT =====")
    print("1 - Tra từ điển")
    print("2 - Thêm từ điển")
    print("3 - Xóa từ điển")
    print("4 - Thoát chương trình")

def tra_tu_dien(dictionary):
    while True:
        tu = input("\nNhập từ tiếng Anh cần tra (hoặc 0 để quay lại menu): ").strip().lower()
        if tu == "0":
            break
        if tu in dictionary:
            print(f"Nghĩa tiếng Việt: {dictionary[tu]}")
        else:
            print("Không tìm thấy từ này trong từ điển.")
        tiep = input("Bạn có muốn tra tiếp không? (y/n): ").strip().lower()
        if tiep != "y":
            break

def them_tu_dien(dictionary):
    while True:
        tu_anh = input("\nNhập từ tiếng Anh (hoặc 0 để quay lại menu): ").strip().lower()
        if tu_anh == "0":
            break
        if tu_anh in dictionary:
            print("Từ này đã có trong từ điển!")
        else:
            nghia_viet = input("Nhập nghĩa tiếng Việt: ").strip()
            dictionary[tu_anh] = nghia_viet
            print("Đã thêm thành công!")
        tiep = input("Bạn có muốn thêm tiếp không? (y/n): ").strip().lower()
        if tiep != "y":
            break

def xoa_tu_dien(dictionary):
    while True:
        tu = input("\nNhập từ tiếng Anh muốn xóa (hoặc 0 để quay lại menu): ").strip().lower()
        if tu == "0":
            break
        if tu in dictionary:
            del dictionary[tu]
            print("Đã xóa thành công!")
        else:
            print("Không tìm thấy từ cần xóa.")
        tiep = input("Bạn có muốn xóa thêm không? (y/n): ").strip().lower()
        if tiep != "y":
            break

# -------------------------------
# Chương trình chính
# -------------------------------
def main():
    tu_dien = {
        "hello": "xin chào",
        "goodbye": "tạm biệt",
        "book": "quyển sách",
        "apple": "quả táo"
    }

    while True:
        print()
        menu()
        try:
            chon = int(input("Chọn chức năng (1-4): "))
        except ValueError:
            print("Vui lòng nhập số từ 1 đến 4!")
            continue

        if chon == 1:
            tra_tu_dien(tu_dien)
        elif chon == 2:
            them_tu_dien(tu_dien)
        elif chon == 3:
            xoa_tu_dien(tu_dien)
        elif chon == 4:
            print("\nCảm ơn bạn đã sử dụng TỪ ĐIỂN ANH VIỆT! Hẹn gặp lại ❤️")
            break
        else:
            print("Lựa chọn không hợp lệ! Vui lòng nhập lại.")

if __name__ == "__main__":
    main()

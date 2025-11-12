#===== TỪ ĐIỂN ANH VIỆT =====
def menu():
    print("===== TỪ ĐIỂN ANH - VIỆT =====")
    print("1 - Tra từ điển")
    print("2 - Thêm từ điển")
    print("3 - Xóa từ điển")
    print("4 - Thoát chương trình")

def tra_tu(dictionary):
    while True:
        n = input('Nhap tu can tra').strip().lower()
        if n == 0:
            break
        if n in dictionary:
            print(dictionary['n'])
        else:
            print('Tu nay khong co trong tu dien')

def them_tu(dictionary):
    while True:
        n = input('Nhap tu tieng Anh').strip().lower()
        
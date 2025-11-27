def xin_chao():
    print('xin chao toi la ABC')

def say_hello(name):
    print('xin chao', name)

def phep_toan(a, b):
    print('tong = ', a + b)

def tham_so_mac_dinh(num = 10):
    print('Hello')

def tong(*number):
    print(sum(number))

xin_chao()
say_hello('Duong')
phep_toan(10, 22)
tham_so_mac_dinh()
tong(1, 2, 3, 4, 5, 6, 7, 8, 9)
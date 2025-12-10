sv = int(input())
for i in range(sv):
    msv= input()
    name = input()
    clas = input()
for j in range(sv):
    dihoc = input()
    dck = 10
    for k in dihoc:
        if k == 'm':
            dck -= 1
        elif k == 'v':
            dck -= 2
    print(msv, name, clas, dck)
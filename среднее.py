f = open('9-9.txt')
ka = 0#удовл
ko = 0#общ
for s in f:
    a = [int(x) for x in s.split()]
    ko += 1
    kol = []
    for i in range(len(a)):
        kol.append(a.count(a[i]))
    if kol.count(1) == 1 and kol.count(2) == 2 and kol.count(3) == 3:
        sk = 0
        vsebez1 = sum(a)
        for i in range(len(a)):
            if int(str(a[i])[0]) % 2 == 1:
                sk += a[i]**2
            if kol[i] == 1:
                vsebez1 -= a[i]
        if sk > vsebez1:
            ka += 1
print(ko - ka)


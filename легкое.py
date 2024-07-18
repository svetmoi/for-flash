f = open('9-5.txt')
otv = 0
for s in f:
    a = [int(x) for x in s.split()]
    a.sort()
    if max(a) % 3 == 0:
        r1 = r2 = r3 = d1 = d2 = d3 = 0
        r1 = abs(a[0] - a[1])
        r2 = abs(a[1] - a[2])
        r3 = abs(a[2] - a[3])
        d1 = a[1]/a[0]
        d2 = a[2]/a[1]
        d3 = a[3]/a[2]
        if (r1 == r2 and r2 == r3) or (d1 == d2 and d2 == d3):
            otv = sum(a)/len(a)
print(otv)#не забыть про то, что надо только целую часть

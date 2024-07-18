def st(n):
    s = 0
    tn = 0
    while tn < n:
        tn = 2**s
        if tn == n:
            return 1
        s += 1
    if tn != n:
        return 0
        

f = open('9-9.txt')
k = []
for s in f:
    a = [int(x) for x in s.split()]
    if st(max(a)) == 1:
        k7 = k11 = ost = sumch = 0
        if str(a[0])[0] == '7':
            k7 += 1
        elif str(a[0])[:2] == '11':
            k11 += 1
        ost = a[0] % 2
        if ost == 0:
            sumch += a[0]
        for i in range(1,len(a)):
            if a[i] % 2 == ost:
                break
            else:
                ost = a[i] % 2
                if ost == 0:
                    sumch += a[i]
                if str(a[i])[0] == '7':
                    k7 += 1
                elif str(a[i])[:2] == '11':
                    k11 += 1
        else:
            if k7 >= k11:
                if sumch not in k:
                    k.append(sumch)
print(len(k))

s = open('26_5_1.txt')
N = int(s.readline())
a = [z.split() for z in s]
a = sorted(set([(int(x), int(y)) for x, y in a]))
strok = sorted([z[0] for z in a])
d = {d:0 for d in strok}
n = 1
for z in range (1, len(a)):
    r0, m0 = a[z-1]
    r1, m1 = a[z]
    if r0 == r1 and m1 - m0 == 2:
        n = n + 1
        d[r0] = max(d[r0], n)
    else:
        n = 1
pa = max([z for z in d.values()])
pb = min(z for z in d.keys() if d[z] == pa)
print(pa, pb)
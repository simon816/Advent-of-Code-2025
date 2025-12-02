import sys

ranges = [tuple(map(int, l.split('-'))) for l in sys.stdin.readline().split(',')]

inv = 0

for r in ranges:
    for n in range(r[0], r[1] + 1):
        s = str(n)
        l = len(s)
        for i in range(1, l):
            seq = s[:i]
            match = True
            p = i
            while p < l:
                if s[p:p+i] != seq:
                    match = False
                p += i
            if match:
                inv += n
                break

print(inv)

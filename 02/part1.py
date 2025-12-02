import sys

ranges = [tuple(map(int, l.split('-'))) for l in sys.stdin.readline().split(',')]

inv = 0

for r in ranges:
    for n in range(r[0], r[1] + 1):
        s = str(n)
        l = len(s)
        if l % 2 == 0 and s[:l//2] == s[l//2:]:
            inv += n

print(inv)

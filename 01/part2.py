import sys

dial = 50

count = 0

for line in sys.stdin.readlines():
    l = line.strip()
    dir = l[0]
    dist = int(l[1:])

    if dir == 'L':
        n = -1
    else:
        n = 1

    for _ in range(dist):
        dial += n
        if dial == -1:
            dial = 99
        elif dial == 100:
            dial = 0
        if dial == 0:
            count += 1

print(count)

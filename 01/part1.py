import sys

dial = 50

count = 0

for line in sys.stdin.readlines():
    l = line.strip()
    dir = l[0]
    dist = int(l[1:])

    if dir == 'L':
        dial = (dial - dist) % 100
    else:
        dial = (dial + dist) % 100

    if dial == 0:
        count += 1

print(count)

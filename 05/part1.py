import sys


ranges = set()
available = set()
read_ranges = True
for line in sys.stdin.readlines():
    line = line.strip()
    if not line:
        read_ranges = False
        continue
    if read_ranges:
        ranges.add(tuple(map(int, line.split('-'))))
    else:
        available.add(int(line))

fresh = 0

for ing in available:

    for (start, end) in ranges:
        if ing >= start and ing <= end:
            fresh += 1
            break

print(fresh)

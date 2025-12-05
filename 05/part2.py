import sys

ranges = set()
for line in sys.stdin.readlines():
    line = line.strip()
    if not line:
        break
    ranges.add(tuple(map(int, line.split('-'))))


last_end = 0

size = 0

for (start, end) in sorted(ranges):
    if start <= last_end:
        start = last_end + 1
    if end < start:
        continue
    gap = end - start
    size += gap + 1
    last_end = end

print(size)

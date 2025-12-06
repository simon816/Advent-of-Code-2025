from collections import defaultdict
import re
import sys

lists = defaultdict(list)
operations = []

lines = []

for line in sys.stdin.readlines():
    lines.append(line.strip('\n'))

max_len = max(map(len, lines))

buffer = []
total = 0

for i in range(max_len - 1, -1, -1):
    slice = [l[i] for l in lines]
    op = None
    if slice[-1] in '+*':
        op = slice[-1]
        slice = slice[:-1]
    rejoined = ''.join(slice).strip()
    if not rejoined:
        continue
    buffer.append(int(rejoined))
    if op is not None:
        if op == '*':
            t = 1
            for n in buffer:
                t *= n
            total += t
        else:
            total += sum(buffer)
        buffer = []

print(total)

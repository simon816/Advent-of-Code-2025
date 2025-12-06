from collections import defaultdict
import re
import sys

lists = defaultdict(list)
operations = []

for line in sys.stdin.readlines():
    cols = re.split(' +', line.strip())
    if cols[0] in '*+':
        operations = cols
    else:
        for i, n in enumerate(cols):
            lists[i].append(int(n))

total = 0
for i in range(len(operations)):
    op = operations[i]
    if op == '*':
        t = 1
        for n in lists[i]:
            t *= n
        total += t
    else:
        total += sum(lists[i])

print(total)

import sys

total = 0

for line in sys.stdin.readlines():
    bank = [int(n) for n in line.strip()]

    n = 0
    start = 0
    for left in range(11, -1, -1):
        if left == 0:
            candidates = bank[start:]
        else:
            candidates = bank[start:-left]
        largest = max(candidates)
        pos = candidates.index(largest)
        pos += start
        start = pos + 1
        n += bank[pos] * (10 ** left)
    total += n

print(total)
    

import sys

total = 0

for line in sys.stdin.readlines():
    bank = [int(n) for n in line.strip()]
    largest = max(bank)
    pos1 = bank.index(largest)
    if pos1 == len(bank) - 1:
        pos2 = pos1
        largest = max(bank[:pos2])
        pos1 = bank.index(largest, 0, pos2)
    else:
        largest = max(bank[pos1+1:])
        pos2 = bank.index(largest, pos1+1)
    n = (bank[pos1] * 10) + bank[pos2]
    total += n

print(total)
    

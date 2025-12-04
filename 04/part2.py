import sys

grid = []

for line in sys.stdin.readlines():
    grid.append(list(line.strip()))

def can_remove(r, c):
    neighbours = 0
    if grid[r][c] != '@':
        return False

    if c > 0 and row[c-1] == '@':
        neighbours += 1
    if c < len(row)-1 and row[c+1] == '@':
        neighbours += 1
    if r > 0 and grid[r-1][c] == '@':
        neighbours += 1
    if r < len(grid)-1 and grid[r+1][c] == '@':
        neighbours += 1
    if c > 0 and r > 0 and grid[r-1][c-1] == '@':
        neighbours += 1
    if c > 0 and r < len(grid)-1 and grid[r+1][c-1] == '@':
        neighbours += 1
    if c < len(row)-1 and r > 0 and grid[r-1][c+1] == '@':
        neighbours += 1
    if c < len(row)-1 and r < len(grid)-1 and grid[r+1][c+1] == '@':
        neighbours += 1

    return neighbours < 4


did_change = True
count = 0
while did_change:
    did_change = False
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if can_remove(r, c):
                grid[r][c] = '.'
                did_change = True
                count += 1
print(count)

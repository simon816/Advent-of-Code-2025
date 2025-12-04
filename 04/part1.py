import sys

grid = []

count = 0

for line in sys.stdin.readlines():
    grid.append(list(line.strip()))

for r, row in enumerate(grid):
    for c, cell in enumerate(row):
        neighbours = 0
        if cell != '@':
            continue
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

        if neighbours < 4:
            count += 1
print(count)

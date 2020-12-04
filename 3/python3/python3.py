grid = [list(s.strip()) for s in open('../input.txt').readlines()]

for line in grid:
    for i in range(7):
        line.extend(line)

def trees(offset_x, offset_y):
    trees = x = y = 0

    while y < len(grid) and x < len(grid[0]):
        if grid[y][x] == '#':
            trees += 1

        x += offset_x
        y += offset_y

    return trees

print(trees(3, 1))
print(trees(1, 1) * trees(3, 1) * trees(5, 1) * trees(7, 1) * trees(1, 2))

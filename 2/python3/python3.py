import re

prog = re.compile(r'(\d+)-(\d+) (\w): (\w+)')

lines = [prog.match(l).groups() for l in open('../input.txt').readlines()]
lines = [[int(x), int(y), c, s] for x, y, c, s in lines]

old = new = 0

for x, y, c, s in lines:
    if x <= s.count(c) <= y: old += 1
    if (s[x-1] == c) != (s[y-1] == c): new += 1

print(str(old) + ', ' + str(new))

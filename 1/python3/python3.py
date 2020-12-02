from itertools import combinations
from math import prod

entries = [int(i) for i in open('../input.txt')]

def find_combination(amount_of_entries):
    for c in combinations(entries, amount_of_entries):
        if sum(c) == 2020: return str(prod(c))

print(find_combination(2) + ', ' + find_combination(3))

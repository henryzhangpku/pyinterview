import itertools
friends = ['Monique', 'Ashish', 'Devon', 'Bernie']
print(list(itertools.permutations(friends, r=2)))

print(list(itertools.combinations(friends, r=2)))
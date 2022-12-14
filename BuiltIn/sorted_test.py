print(sorted([6,5,3,7,2,4,1]))
print(sorted(['cat', 'dog', 'cheetah', 'rhino', 'bear'], reverse=True))

animals = [
{'type': 'penguin', 'name': 'Stephanie', 'age': 8},
{'type': 'elephant', 'name': 'Devon', 'age': 3},
{'type': 'puma', 'name': 'Moe', 'age': 5},
]
print(sorted(animals, key=lambda animal: animal['age']))
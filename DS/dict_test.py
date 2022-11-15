cowboy = {'age': 32, 'horse': 'mustang', 'hat_size': 'large'}
print(cowboy)
#if exists
name = cowboy.get('name', 'The Man with No Name')
#better
name = cowboy.setdefault('name', 'The Man with No Name')

print(cowboy)
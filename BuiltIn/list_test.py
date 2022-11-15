nums = [4, 2, 1, 6, 9, 7]
print(nums)
def square(x):
	return x*x

print(list(map(square, nums)))

def is_odd(x):
	return bool(x % 2)

print(list(filter(is_odd, nums)))

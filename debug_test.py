nums = [45,22,14,65,97,72]
for i, v in enumerate(nums):
	if v % 3==0 and v % 5 ==0:
		breakpoint()
		nums[i]='fizzbuzz'
	elif v % 3 ==0:
		nums[i]='fizz'
	elif v % 5==0:
		nums[i]='buzz'
print(nums)
for i, v in enumerate(nums, start=52):
	print(i, v)

def count_bits(x):
	ans=0
	while x:
		ans+=x & 1
		x>>=1
	return ans

print(count_bits(10))
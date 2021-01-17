import pandas as pd 

data = pd.read_csv("2sum.txt", header=None)
num_list = data[0].tolist()
print(num_list)
num_set = set(num_list)
A = list(num_set)
A.sort()
sum_set = set()

range_left = -10000
range_right = 10000

left = 0
right = len(A)-1

print("A is ", A)
count = 0
while left < right: 
	count += 1
	print("in iteration ", count, "of while loop")

	if A[left] + A[right] < range_left: 
		left += 1
	elif A[left] + A[right] > range_right:
		right -= 1
	else: 
		for i in range(right, left, -1):
			new_sum = A[left] + A[i]
			if new_sum < range_left: 
				break
			else: 
				sum_set.add(new_sum)
		left += 1

print(sum_set)
print(len(sum_set))







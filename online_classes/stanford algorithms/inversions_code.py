import pandas as pd
import math

data = pd.read_csv("inversions.txt", header=None)
num_list = data[0].tolist()



def inversionsDivideAndConquer(d):
	count_inversions = 0

	# base case: 
	if len(d)==1: 
		return 0
	else: 
		split_ind = math.floor(len(d)/2)
		d_left = d[0: split_ind]
		d_right = d[split_ind : len(d)]

		count_inversions_left = inversionsDivideAndConquer(d_left)
		count_inversions_right = inversionsDivideAndConquer(d_right)
		count_split_inversions = calculateSplitInversions(d_left, d_right)

		count_inversions = count_inversions_right + count_inversions_left + count_split_inversions
		return count_inversions

def calculateSplitInversions(d_left, d_right): 
	merged_array = []
	num_split_inversions = 0
	left_index = 0
	right_index = 0

	d_left.sort()
	d_right.sort()

	while (left_index < len(d_left)) or (right_index < len(d_right)):
		if right_index == len(d_right): 
			merged_array.append(d_left[left_index])
			left_index += 1
		elif left_index == len(d_left): 
			merged_array.append(d_right[right_index])
			right_index += 1	
		elif d_left[left_index] <= d_right[right_index]: 
			merged_array.append(d_left[left_index])
			left_index += 1
		else: # if the right element is larger
			merged_array.append(d_right[right_index])
			right_index += 1
			num_split_inversions += (len(d_left) - left_index)


	return num_split_inversions

t1 = [1, 2, 3, 5, 4, 6]
t2 = [1, 1, 1, 2, 1, 1]
t3 = [1, 1, 1, 1, 1, 10]

t1_count = inversionsDivideAndConquer(t1)
t2_count = inversionsDivideAndConquer(t2)
t3_count = inversionsDivideAndConquer(t3)

print("t1 inversions: ", t1_count)
print("t2 inversions: ", t2_count)
print("t3 inversions: ", t3_count)

d_count = inversionsDivideAndConquer(num_list)
print("data inversions:", d_count)








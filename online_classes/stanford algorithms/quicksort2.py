import pandas as pd
import math

data = pd.read_csv("quicksort.txt", header=None)
num_list = data[0].tolist()

def qs(A, num): 
	if len(A)<=1: 
		return A,0
	else: 
		p = A[0]

	i = 0
	for j in range(1, len(A)):
		if A[j] < p: 
			A[j], A[i] = A[i], A[j]
			i += 1

	A[0], A[i-1] = A[i-1], A[0]

	z = A[:i]
	y = A[i+1:]

	z,zi = qs(z, num)
	y,yi = qs(y, num)
	count = len(A)-1+zi+yi
	
	return z+[p]+y, count

# num_list.reverse()
#list1, count_1 = qs(num_list, 1)
#print("num_comparisons for method 1: ", count_1)

list2, count_2 = qs(num_list, 2)
print("num_comparisons for method 2: ", count_2)

list3, count_3 = qs(num_list, 3)
print("num_comparisons for method 3: ", count_3)


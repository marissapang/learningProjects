import pandas as pd
import math

data = pd.read_csv("quicksort.txt", header=None)
num_list = data[0].tolist()


def quickSort(data, pivot_num):

	num_comparisons = 0

	if len(data) <= 1:
		return 0
	else: # recursive call	
		p_ind = getPivot(pivot_num, data)

		if p_ind != 0: 
			data[p_ind], data[0] = data[0], data[p_ind]


		pivot = data[0]

		i = 0 + 1

		for j in range(1, len(data)):
			if data[j] < pivot: 
				# switch data[i] and data[j]
				data[i], data[j] = data[j], data[i]
				i += 1
		
		data[0], data[i-1] = data[i-1], data[0]

		# recursive call on smaller
		left_data = data[0:i-1]
		right_data = data[i:len(data)]
		left_comparisons = quickSort(left_data, pivot_num)
		right_comparisons = quickSort(right_data, pivot_num)

		num_comparisons += len(left_data) + len(right_data)
		num_comparisons += left_comparisons + right_comparisons

		return num_comparisons

def getPivot(pivot_num, data): 
	if pivot_num == 1: 
		p_ind = 0
	elif pivot_num == 2: 
		p_ind = -1
	elif pivot_num == 3: 
		first = data[0]
		last = data[-1]
		mid = data[getMiddleIndex(len(data))]

		if (first <= mid <= last) or (last <= mid <= first): 
			p_ind = getMiddleIndex(len(data))
		elif (mid <= first <= last) or (last <= first <= mid): 
			p_ind = 0
		elif (mid <= last <= first) or (first <= last <= mid): 
			p_ind = -1

	return p_ind



def getMiddleIndex(array_length):
	middleIndex = math.ceil(array_length / 2) - 1
	return middleIndex


# t1 = [6, 83, 5, 20, 50, 90, 4, 3, 2, 1, 10, 11, 15, 95, 55, 35]
# t1 = [1,2,3,4,5]
t1 = [3, 5, 2, 1, 6]

count_t1 = quickSort(t1,2)
print(count_t1)

# num_list.reverse()
# count_1 = quickSort(num_list, 1)
# print("num_comparisons for method 1: ", count_1)

# count_2 = quickSort(num_list, 2)
# print("num_comparisons for method 2: ", count_2)

count_3 = quickSort(num_list, 3)
print("num_comparisons for method 3: ", count_3)



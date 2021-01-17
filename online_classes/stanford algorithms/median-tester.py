import pandas as pd
import math

def simulateArrival():
	data = pd.read_csv("median.txt", header=None)
	num_list = data[0].tolist()

	return num_list

def printMedians():
	count = 0
	num_list = []
	median_list = []
	for num in simulateArrival():
		count += 1
		print("*********************")
		print("*********************")
		print("In number ", count, " of ", len(simulateArrival()), " arrivals")
		print("new arrival is ", num)
		num_list.append(num)
		num_list.sort()
		print("lenght of median list is ", len(num_list))
		median_index = math.ceil(len(num_list)/2)-1
		median_list.append(num_list[median_index])

		# print("the actual median is: ", median_list[median_index])
	final_sum = sum(median_list) % 10000
	print("the final sum is", final_sum)

printMedians()



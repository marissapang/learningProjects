import pandas as pd
import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(10000)

def readData():
	data = pd.read_csv("knapsack_big.txt", header=None)
	capacity = int(data[0].tolist()[0].split(" ")[0])
	data_list = data[0].tolist()[1:]

	output = []
	total_weight = 0

	for item in data_list: 
		item_list = item.split(" ")
		value = int(item_list[0])
		weight = int(item_list[1])
		total_weight += weight
		output.append((value, weight))

	return output, total_weight, capacity


items, total_weight, capacity = readData()

storage = {} # key: (i, x), value: (value, weight)


def fillKnapsack():
	# for the i=0 case: 
	item = items[0]
	next_item = items[1]

	# this is the last best solution + new value for i=1
	key = (0, item[1], True) # i, weight of w0 (implicitly with w1 subtracted), is value added boolean
	value = item[0] + next_item[0]
	storage[key] = value

	# this is the case when last best solution = curr best solution
	key = (0, item[1]+next_item[1], False)
	value = item[0]
	storage[key] = value



def recursiveKnapsack(i, x):
	print("in recursive call for i = ", i, "x = ", x)
	# case if previously calculated: 
	if (i, x) in storage: 
		return storage[(i,x)]

	# base case: 
	if i == 0: 
		if items[i][1] <= x: 
			storage[(0, x)] = items[i]
			return items[i]
		else: 
			return (0, 0)

	# first recursive call for i-1, x

	case1_value, case1_weight = recursiveKnapsack(i-1, x)
	if case1_weight > capacity: 
		case1_value = 0

	if x-items[i][1] > 0: 
		case2_value, case2_weight = 0, 0
		case2_value, case2_weight= recursiveKnapsack(i-1, x-items[i][1]) 
		case2_value += items[i][0]
		case2_weight +=  items[i][1]

		if case2_weight > capacity: 
			case2_value = 0
	else: 
		case2_value = 0

	if case1_value >= case2_value: 
		answer = (case1_value, case1_weight)
	else: 
		answer = (case2_value, case2_weight)


	storage[(i, x)] = answer

	return answer




answer = recursiveKnapsack(len(items)-1, capacity)

print("capcity is: ", capacity)
print(answer)




import pandas as pd
import math

left_heap = [] # structured where the first index is the root, in this case the max
right_heap = [] # structured where the first index is the root, in this case the min
median_list = []

def simulateArrival():
	data = pd.read_csv("small-median.txt", header=None)
	num_list = data[0].tolist()

	return num_list

def performInsertion(value):
	if len(left_heap) == 0: 
		left_heap.append(value)
		return "left"
	elif len(right_heap) == 0: 
		right_heap.append(value)
		return "right"
	elif value <= left_heap[0]: 
		left_heap.append(value)
		return "left"
	else: 
		right_heap.append(value)
		return "right"

def findParentIndex(child_index):
	if child_index == 0: 
		raise Error("somehow we are trying find a parent for a 0 node")

	child_level = math.floor(math.log2(child_index))
	# print("child_level is", child_level)
	child_level_start = 2**child_level - 1
	child_position_on_level = child_index - child_level_start + 1


	parent_position_on_level = math.ceil(child_position_on_level/2)
	#print("parent_position_on_level is", parent_position_on_level)
	parent_level = child_level - 1
	#print("parent_level is", parent_level)

	parent_index = 2**parent_level - 1 + parent_position_on_level - 1

	#print("parent is: ", parent_index)
	return int(parent_index)


def maintainInvariantForHeaps(heap_type):
	if len(left_heap) == 1 and len(right_heap) == 1: 
		if left_heap[0] > right_heap[0]: 
			left_heap[0], right_heap[0] = right_heap[0], left_heap[0]

	if heap_type == "left":
		i = len(left_heap) - 1

		while i > 0: 
			# keep looking for parents
			current = left_heap[i]
			parent_index = findParentIndex(i)
			parent = left_heap[parent_index]

			if parent < current: 
				left_heap[parent_index], left_heap[i] = left_heap[i], left_heap[parent_index]
				i = parent_index
			else: 
				break
	elif heap_type == "right": 
		i = len(right_heap) - 1

		while i > 0: 
			# keep looking for parents
			current = right_heap[i]
			parent_index = findParentIndex(i)
			parent = right_heap[parent_index]

			if parent > current: 
				right_heap[parent_index], right_heap[i] = right_heap[i], right_heap[parent_index]
				i = parent_index
			else: 
				break

	else: 
		raise Exception("heap_type is not left or right")
	# for the last element, keep switching until you get to the correct number




def rebalanceHeaps(): 
	if abs(len(left_heap) - len(right_heap)) <= 1: #if heaps are balanced
		() # do nothing
	elif len(left_heap) - len(right_heap) >= 2: # if left heap is larger in size
		if left_heap[1] < left_heap[2]: 
			num_levels = math.floor(math.log2(len(left_heap)))
			for k in range(1, num_levels+1):
				left_ind = int(2**k-1)
				mid_ind = min(left_ind + int((2**k)/2), len(left_heap))
				right_ind = min(left_ind + int(2**k), len(left_heap))

				print("k is", k) 
				print("left_ind is ", left_ind)
				print("mid_ind is ", mid_ind)
				print("right_ind is ", right_ind)
				print("left_heap is", left_heap)

				print("right now, the mid index is ", mid_ind, " and the right index is ", right_ind)
				
				if (mid_ind != right_ind):
					left_heap[left_ind:mid_ind], left_heap[mid_ind: right_ind] = left_heap[mid_ind: right_ind],left_heap[left_ind:mid_ind]


			if right_heap[0] < right_heap[1]: 
				right_heap[0], right_heap[1] = right_heap[1], right_heap[0]
			elif right_heap[0] < right_heap[2]: 
				right_heap[0], right_heap[2] = right_heap[2], right_heap[0]

		# then we shift the max value to be the min of the right heap
		value = left_heap.pop(0)
		right_heap.insert(0, value)

	elif len(right_heap) - len(left_heap) >= 2: # if right heap is larger in size
		print("LOOK HERE: right_heap is: ", right_heap)
		if right_heap[1] > right_heap[2]: 
			print("INSIDE THIS IF STATEMENT")
			num_levels = math.floor(math.log2(len(right_heap)))
			for k in range(1, num_levels + 1):
				if k == num_levels and 2**(k+1)-1 != len(right_heap):
					next

				left_ind = int(2**k-1)
				mid_ind = min(left_ind + int((2**k)/2), len(right_heap))
				# right_ind = min(int(2**(k+1)-1), len(right_heap))
				right_ind = min(left_ind + int(2**k), len(right_heap))
				print("k is", k) 
				# print("left_ind is ", left_ind)
				# print("mid_ind is ", mid_ind)
				# print("right_ind is ", right_ind)
				# print("right_heap is", right_heap)

				print("left_ind is ", left_ind, ", mid_ind is ", mid_ind, " and right_ind is", right_ind)

				if (mid_ind != right_ind):
					right_heap[left_ind:mid_ind], right_heap[mid_ind: right_ind] = right_heap[mid_ind: right_ind],right_heap[left_ind:mid_ind]
					print("switch was performed, and post switch the right heap is")
					print(right_heap)


			# if k the entire level is full then we are good
			if 2**(k+1)-1 != len(right_heap)
			# if not the entier level is full then we just iterate through through each index to try to get it ok

			if left_heap[0] < left_heap[1]: 
				left_heap[0], left_heap[1] = left_heap[1], left_heap[0]
			elif left_heap[0] < left_heap[2]: 
				left_heap[0], left_heap[2] = left_heap[2], left_heap[0]


		value = right_heap.pop(0)
		left_heap.insert(0, value)



def findMedian():
	if len(left_heap) == len(right_heap): 
		median = left_heap[0]
	elif len(left_heap) - len(right_heap) == 1: 
		median = left_heap[0]
	elif len(right_heap) - len(left_heap) == 1: 
		median = right_heap[0]
	else: 
		raise Exception("left and right heap are not balanced at findMedian function call")

	median_list.append(median)




def mainFunction():
	count = 0
	for num in simulateArrival():
		count += 1
		print("**********************")
		print("In number ", count, " of ", len(simulateArrival()), " of arrivals")
		print('new arrival is ', num)
		print("")

		# append num to right or left heap and perform heap operations
		heap_type = performInsertion(num)
		maintainInvariantForHeaps(heap_type)
		rebalanceHeaps()
		heap_type = "" # reset heap type just in case somehting is going wrong

		findMedian()

		print("AT THE END, the left heap is of length", len(left_heap))
		print(left_heap)
		print("and the right heap is of length", len(right_heap))
		print(right_heap)
		print("our calculated median is: ", median_list[-1]) 
		print("********************")

		



	median_sum = 0
	for median in median_list: 
		median_sum += median

	median_mod = median_sum % 10000

	median_mod2 = sum(median_list) % 10000

	print("MEDIAN MOD IS")
	print(median_mod)
	print(median_mod2)

		# at this point, ehaps should be balanced, so we can calculate median

# x = [10, 7, 9, 6, 5, 8, 7, 3, 2, 1, 4, 7]
# findParentIndex(2)

mainFunction()






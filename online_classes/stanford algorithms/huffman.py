import pandas as pd
import sys
sys.setrecursionlimit(1500)

def constructData():
	data = pd.read_csv("small-huffman.txt", header=None)
	data_list = data[0].tolist()
	data_list = data_list[1:]

	freq_list = [] # list of tuples (frequency, [list of labels in group])
	code_dict = {}
	for i in range(len(data_list)): 
		freq = data_list[i]
		freq_list.append((freq, [i]))
		code_dict[i] = "" # initialize all code with 0

	print(freq_list[0:20])

	return freq_list, code_dict

freq_list, code_dict = constructData()

def recursiveHuffman():
	# base case: when there are only 2 groups left
	if len(freq_list) == 2: 
		return

	# get the two items with the lowest frequency
	print("freq_list length is :", len(freq_list))
	freq_list.sort(key=lambda x: x[0], reverse=True)
	f1, l1 = freq_list.pop()
	f2, l2 = freq_list.pop()

	# combine them into a single frequency
	new_freq = f1+f2
	new_label_list = l1+l2
	freq_list.append((new_freq, new_label_list))

	# on the shortened list, make recursive call
	recursiveHuffman()

	# append 0 and 1s to corresponding labels
	for label in l1:
		code_dict[label] = code_dict[label]+"0"

	for label in l2: 
		code_dict[label] = code_dict[label]+"1"


def findMinAndMaxLength():
	max_length = 0
	min_length = 100000000000000
	for label, code in code_dict.items():
		max_length = max(max_length, len(code))
		min_length = min(min_length, len(code))


	print(code_dict)




recursiveHuffman()
findMinAndMaxLength()






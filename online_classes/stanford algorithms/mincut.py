import pandas as pd
import math
import random

def makeAdjDict():
	data = pd.read_csv("mincut.txt", header=None)
	data_list = data[0].tolist()

	# define adj list data structure
	adj_dict = {} #key: vertex label, value: list of neighbors
	
	for line in data_list: 
		line_list = line.split('\t')
		v = line_list.pop(0)

		if line_list[-1] == '': 
			line_list.pop(-1)

		adj_dict[v] = line_list

	return adj_dict

def makeEdgeList(adj_dict): 
	edge_list = [] #list of tuples (v1, v2
	for v, e_list in adj_dict.items(): 
		for e in e_list: 
			edge_list.append((v, e))

	return edge_list

def pickRandomEdge(edge_list):
	return random.choice(edge_list)

def edgeReverse(edge): 
	return (edge[1], edge[0])

def updateEdgeList(edge_list, edge):
	v1 = edge[0]
	v2 = edge[1]

	len_before = len(edge_list)

	# remove the edge we just picked from the edge list in both directions
	edge_list = [e for e in edge_list if (e != edge and e != edgeReverse(edge))]

	len_after = len(edge_list)

	# change all the things that link to v2 to link to v1 instead now
	for i in range(len(edge_list)):
		if edge_list[i][0] == v2: 
			edge_list[i] = (v1, edge_list[i][1])
		if edge_list[i][1] == v2: 
			edge_list[i] = (edge_list[i][0], v1)
	return edge_list

def updateAdjDict(edge, adj_dict):
	v1 = edge[0]
	v2 = edge[1]
	v1_neighbors = adj_dict[v1]

	if v2 in adj_dict:
		v2_neighbors = adj_dict[v2]
	else: 
		v2_neighbors = []

	combined_neighbors = v1_neighbors + v2_neighbors
	# filter to remove anything that links to itself, which is v1 or v2
	combined_neighbors = [n for n in combined_neighbors if n != v1 and n != v2]

	# add this new entry to v1
	adj_dict[v1] = combined_neighbors

	# remove v2
	if v2 in adj_dict:
		adj_dict.pop(v2) # only remove one of the entries

	# change all things that link to v2 to link to v1 instead
	for v, e_list in adj_dict.items():
		for i in range(0, len(e_list)): 
			if e_list[i] == v2: 
				e_list[i] = v1
		adj_dict[v] = e_list

	return adj_dict

def calculateUniqueEdges(edge_list):
	counting_list = list(set(edge_list))

	return len(counting_list)


def performOneContraction(adj_dict, edge_list): 

	# pick edge
	random_edge = pickRandomEdge(edge_list)

	#remove BOTH entries of the edge from edge_list
	edge_list = updateEdgeList(edge_list, random_edge)

	# update the adj_dict
	adj_dict = updateAdjDict(random_edge, adj_dict)

	return (adj_dict, edge_list)


		
def contractionAlgorithm(): 
	random.seed()

	adj_dict = makeAdjDict()
	edge_list = makeEdgeList(adj_dict)

	count = 0

	while calculateUniqueEdges(edge_list) > 2: 
		count += 1
		adj_dict, edge_list = performOneContraction(adj_dict, edge_list)

	# print("**** ANSWER*****")
	# for v in adj_dict: 
	# 	print("for vertex: ", v)
	# 	print("thhere are ", len(adj_dict[v]), "number of edges")

	# print("the edge_list is of length ", len(edge_list))

	if len(edge_list) % 2 != 0: 
		raise Exception("The edgelist is odd in length")

	min_cut = len(edge_list)/2

	return min_cut


def runManyTests(num_iterations):

	answer_list = []

	for i in range(num_iterations):
		print("in iteration #", i)
		
		answer_list.append(contractionAlgorithm())
		# print("answer list looks like this")
		# print(answer_list)

		print("at this point, the min number is ", min(answer_list))

	
	return min(answer_list)

	
	


runManyTests(500)








# adj_dict = makeAdjDict()
# edge_list = makeEdgeList(adj_dict)
# reverse_list = []
# for i in range(len(edge_list)): 
# 	reverse_list.append(edgeReverse(edge_list[i]))
# edge_list = edge_list + reverse_list

# print(edge_list)
# random_edge = pickRandomEdge(edge_list)
# print("random choice is: ", random_edge[0])
# print(updateEdgeList(edge_list, random_edge))



# need to remove double-counting edges in edge or do we - we probably don't for picking



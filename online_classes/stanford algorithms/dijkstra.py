import pandas as pd
import math
import random

def makeAdjList():
	data = pd.read_table("dijkstra.txt", header=None, sep='a', delimiter=None)
	data_list = data[0].tolist()

	# define adj list data structure
	adj_dict = {} #{tail_node: {head_node: distance from tail to head}}
	adj_list = [] #[{head_node: distance from index+1 to head}]
	
	for line in data_list: 
		line_list = line.split('\t')
		if line_list[-1] == '': 
			line_list.pop(-1)
		tail = int(line_list.pop(0))

		for pair in line_list:
			pair_list = pair.split(',')
			head = int(pair_list[0])
			distance = int(pair_list[1])

			if tail in adj_dict:
				curr_heads = adj_dict[tail]
				curr_heads[head] = distance
				adj_dict[tail] = curr_heads
			else: 
				adj_dict[tail] = {head: distance}

	return adj_dict, adj_list

# global variables
adj_dict, adj_list = makeAdjList()
A = [None]*len(adj_dict)
X = set()


def addNextNode():
	greedy_score_list = []
	greedy_score_nodes = []

	print("in this iteration, X is ", X)
	for node in X: # everything in the set we've looked at
		# print("in node ", node)

		neighbors = adj_dict[node] # dictionary of neighbors as keys and dist from node as values

		print("right now, we are looking at node ", node, " of X")
		print("and its neighbors are: ", neighbors)
		dist_list = []
		dist_nodes = []

		# only look at the set V-X
		neighbors_not_in_X = {}
		for n, dist in neighbors.items():
			if n not in X: 
				neighbors_not_in_X[n] = dist

		print("out of all the neighbors, these are in the set V-X: ", neighbors_not_in_X)


		# print("neighbor_nox_in_X is", neighbors_not_in_X)
		if len(neighbors_not_in_X) == 0: 
			print("because there are no neighbors not already in X for this node, we just go to the next one")
			# do nothing
			()
		else: 
			print("we will iterate through all the neighbors not in X and calculate their dist")
			for n, dist in neighbors_not_in_X.items(): 
				# print("in iteration ", n, "with distacnce", dist)
				dist_nodes.append(n)
				dist_list.append(dist)

			print("the dist_list is ", dist_list)
			print("corresponding to ", dist_nodes)

			# get min of distance in all neighbors of given node
			min_dist = min(dist_list)
			min_ind = dist_list.index(min_dist)
			min_dist_node = dist_nodes[min_ind]

			print("min_dist is: ", min_dist)
			print("mindist_node is: ", min_dist_node)

			# calculate greedy score
			min_greedy_score = A[node-1] + min_dist
			min_greedy_score_node = min_dist_node

			greedy_score_list.append(min_greedy_score)
			greedy_score_nodes.append(min_greedy_score_node)
			print("updated greedy_score_list to be: ", greedy_score_list)
			print("updated greedy_score_nodes to be: ", greedy_score_nodes)


	min_greedy_score = min(greedy_score_list)
	min_greedy_score_ind = greedy_score_list.index(min_greedy_score)
	min_greedy_score_node = greedy_score_nodes[min_greedy_score_ind]

	print("finished looping through all nodes currently in X, and have selected next node")

	print("next node is:",min_greedy_score_node)
	print("ndex node's SP value is: ", min_greedy_score)

	X.add(min_greedy_score_node)
	A[min_greedy_score_node-1] = min_greedy_score

	print("at the end of the iteration X is: ", X, " and A is: ", A)


def dijkstra(s):
	A[s-1] = 0
	X.add(s)
	count = 1
	
	while len(X) < len(A):
		print("this is iteration number ", count)
		addNextNode()
		count += 1

	#print(X)
	print(A)
	
	# start from s, and gradually expand the fronteries

def getRelevantPaths(array):
	shortest_path = []
	big_string = ""

	for v in array: 
		shortest_path.append(A[v-1])
		big_string += str(A[v-1])
		big_string += ","

	print(shortest_path)

	print("***************************")
	print("***************************")
	print("***************************")
	print(big_string)





dijkstra(1)

getRelevantPaths([7, 37, 59, 82, 99, 115, 133, 165, 188, 197])





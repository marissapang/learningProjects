import pandas as pd
import math
import collections

def makeVertices(tail_list, head_list): 
	return list(set(tail_list + head_list))

def makeAdjList(tail_list, head_list):
	if (len(tail_list) != len(head_list)):
		raise Exception("tail list and head list is not the same length")

	adj_list = {}

	for i in range(len(tail_list)):
		tail = tail_list[i]

		if tail in adj_list:
			curr_neighbors = adj_list[tail]
			curr_neighbors.append(head_list[i])
			adj_list[tail] = curr_neighbors
		else: 
			adj_list[tail] = [head_list[i]]

	return adj_list

##### Gobal variables #####
# create graph from data
data = pd.read_csv("SCC.txt", header=None, delimiter=" ")
tail_list = data[0].tolist()
head_list = data[1].tolist()

vertices = makeVertices(tail_list, head_list)
edges_G = makeAdjList(tail_list, head_list)
edges_GRev = makeAdjList(head_list, tail_list)


explored = [False]*len(vertices)
leaders = [0]*len(vertices)
finishings = [0]*len(vertices)
counter = [0]

################

print("made graph representations")



def DFS(vertices, adj_list, v, leader):
	dfs_stack = []

	if explored[v-1] == False:
		dfs_stack.append(v)

	while len(dfs_stack)>0: 
		finished = True
		v = dfs_stack[-1]

		if explored[v-1] == False: 
			explored[v-1] = True
			leaders[v-1] = leader;

			if v in adj_list: 
				neighbors = adj_list[v]
			else: 
				neighbors = []

			for n in neighbors: 
				if explored[n-1] == False:
					dfs_stack.append(n)
					finished = False

		if finished: 
			dfs_stack.pop()

			if finishings[v-1] == 0: 
				counter[0] += 1
				finishings[v-1] = counter[0]

def findSCC():
	# 1. go through G-Rev and do DFS, getting finishing orders
	for v in vertices: 
		if explored[v-1] == True: 
			next
		
		# first DFS call to get ordering, and create finishing order
		DFS(vertices, edges_GRev, v , v)

	print("finished first DFS call")
	
	# 1.5 create a list of tuples to sort through finshing order
	tuple_list = [] 
	for i in range(len(vertices)):
		tuple_list.append((finishings[i], i+1)) # tuple is (finishing order, node label)

	tuple_list.sort(key=lambda x: x[0])


	nodes_in_finishing_order = []
	for order, v in tuple_list: 
		nodes_in_finishing_order.append(v)

	nodes_in_finishing_order.reverse()
	
	print("re-ordered the nodes by finishing order")
	print(nodes_in_finishing_order[0:100])

	#2. go through G in reverse finishing order and do DFS, getting leaders
	for i in range(len(explored)):
		explored[i] = False
		leaders[i] = 0

	print("finshed the processing step")


	for v in nodes_in_finishing_order: 
		if explored[v-1] == True: 
			next
		DFS(vertices, edges_G, v, v)

	print("finished second DFS call")


def countFrequency():
	freq = collections.Counter(leaders)

	#print(freq)
	#print(len(freq))
	print(freq.most_common(5))


findSCC()
countFrequency()






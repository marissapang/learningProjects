import pandas as pd
import math
import gc
import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(100000)
sys.settrace
import resource

resource.setrlimit(
    resource.RLIMIT_CORE,
    (resource.RLIM_INFINITY, resource.RLIM_INFINITY))

# create graph from data
data = pd.read_csv("SCC.txt", header=None, delimiter=" ")
tail_list = data[0].tolist()
head_list = data[1].tolist()



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



vertices = makeVertices(tail_list, head_list)
edges_G = makeAdjList(tail_list, head_list)
adj_list = makeAdjList(head_list, tail_list)

print("G and GRev are created")


explored_tracker = {}
for v in vertices: 
	explored_tracker[v] = False

ordering_stack = []
dfs_stack = []

count = [0]

#def DFS(v, adj_list, explored_tracker, ordering_stack):
def DFS(v):
	count[0] += 1
	print("count is now: ", count)

	if v not in adj_list: # means this node doesn't have any edges
		return

	unexplored_neighbors = []
	for n in adj_list[v]: 
		if explored_tracker[n] == False:
			unexplored_neighbors.append(n)

	if len(unexplored_neighbors) == 0: 
		ordering_stack.append(v)
		return

	for n in unexplored_neighbors: 	
		explored_tracker[n] = True
		DFS(n)

	ordering_stack.append(v)
	return




def findSCCbad():

	# create graph from data
	data = pd.read_csv("SCC.txt", header=None, delimiter=" ")
	tail_list = data[0].tolist()
	head_list = data[1].tolist()

	vertices = makeVertices(tail_list, head_list)
	edges_G = makeAdjList(tail_list, head_list)
	edges_GRev = makeAdjList(head_list, tail_list)
	print("G and GRev are created")

	# go through G-Rev and do DFS, storing the vertices by order of return
	explored_tracker = {}
	for v in vertices: 
		explored_tracker[v] = False
	ordering_stack = []
	dfs_stack = []

	for v in vertices: 
		if explored_tracker[v] == True: 
			next

		dfs_stack.append(v)
		
		while len(dfs_stack) >= 1: 
			curr_v = dfs_stack.pop()

			if v in edges_Grev: 
				curr_neigbhors = edges_GRev[v]
			else: 
				curr_neighbors = []

			unexplored_neighbors = []
			for n in curr_neighbors: 
				if explored_tracker[n] != True: 
					unexplored_neighbors.append(n)

			if len(unexplored_neighbors == 0): 
				ordering_stack.append(v)

			for n in unexplored_neighbors: 
				dfs_stack.append(n)


	print("Went through step 1 of creating ordering_stack")

	print("beginning ordering_stack looks like this: ", ordering_stack[0:10])

def findSCC():
	# go through G-Rev and do DFS, storing the vertices by order of return
	#explored_tracker = [False]*len(vertices)

	for v in vertices:
		if explored_tracker[v] == True: 
			next
		else: 
			explored_tracker[v] = True
			DFS(v)

	print("Went through step 1 of creating ordering_stack")

	print("beginning ordering_stack looks like this: ", ordering_stack[0:10])

findSCC()
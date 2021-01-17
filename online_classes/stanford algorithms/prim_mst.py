import pandas as pd
import math

def createEdgeList(): 
	data = pd.read_csv("prim_mst.txt", header=None)
	data_list = data[0].tolist()
	data_list = data_list[1:]

	edge_list = []
	max_cost = 0
	vertices = set()

	for edge in data_list: 
		tail = int(edge.split(" ")[0])
		head = int(edge.split(" ")[1])
		cost = int(edge.split(" ")[2])	
		edge_list.append((tail, head, cost))
		max_cost = max(max_cost, cost)
		vertices.add(tail)
		vertices.add(head)

	num_vertices = len(vertices)

	print("max_cost is", max_cost, "num_vertices is", num_vertices)
	return edge_list, max_cost, num_vertices

def mainFunction():
	edge_list, max_cost, num_vertices = createEdgeList()

	X = set() # the set of all edges visited

	start = edge_list[0][0]
	X.add(start)
	cost = 0

	while len(X) < num_vertices: 
		print("len(X) is now", len(X))
		min_cost = max_cost+1
		next_node_to_add = None

		for edge in edge_list:
			if (edge[0] in X) and (edge[1] not in X): 
				if edge[2] < min_cost: 
					min_cost = edge[2]
					next_node_to_add = edge[1]
			elif (edge[1] in X) and (edge[0] not in X):
				if edge[2] < min_cost: 
					min_cost = edge[2]
					next_node_to_add = edge[0]

		X.add(next_node_to_add)
		cost += min_cost

	print("final cost is: ", cost)



mainFunction()
	



# pick any vertex to start
# for all vertices in the set X, we look at each edge that coreesponds 
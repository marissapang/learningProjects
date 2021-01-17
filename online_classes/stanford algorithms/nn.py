import pandas as pd

def readData():
	data = pd.read_csv("small-nn.txt", header=None)
	data_list = data[0].tolist()[1:]
	num_vertices = len(data_list)

	vertices = []

	for item in data_list: 
		label = int(item.split(" ")[0])
		x = float(item.split(" ")[1])
		y = float(item.split(" ")[2])
		vertices.append((label, x,y))

	return vertices, num_vertices

vertices, num_vertices = readData()

def calculateSquareDistance(v1, v2):
	x1 = v1[1]
	x2 = v2[1]
	y1 = v1[2]
	y2 = v2[2]

	dist = (x1-x2)**2 + (y1-y2)**2

	return dist

def getFinalDistance(dist_list):
	total_dist = 0

	for d in dist_list: 
		total_dist += d**(1/2)

	return total_dist

def runNNHeuristic():
	# visited = [] # list of vistied vertices
	distance_tracking = [] # list of square distances

	first_vertex = vertices[0]

	start_vertex = first_vertex
	del vertices[0]
	# visited.append(start_vertex)	

	# while len(visited) < len(vertices):
	while len(vertices) > 0:
		print("There are ", len(vertices), "vertices left of ", num_vertices)
		min_distance = float('inf')
		min_index = 0
		for i in range(len(vertices)): 
			v = vertices[i]
			dist = calculateSquareDistance(start_vertex, v)
			if dist < min_distance: 
				min_distance = dist
				min_index = i

		# update to next point
		start_vertex = vertices[min_index]
		# visited.append(start_vertex)
		del vertices[min_index]
		#visited.remove(min_index)
		distance_tracking.append(min_distance)

	# add the final visit back from final point to first point
	distance_tracking.append(calculateSquareDistance(start_vertex, first_vertex))

	# calculate un-suqred total distance
	total_dist = getFinalDistance(distance_tracking)
	print(total_dist)

runNNHeuristic()



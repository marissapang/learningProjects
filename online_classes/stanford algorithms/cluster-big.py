import pandas as pd

def readData():
	data = pd.read_csv("clustering-big.txt", header=None)
	data_list = data[0].tolist()
	data_list = data_list[1:]

	node_set = set()
	cluster_meta = {} # has map of cluster leader to all items in the cluster
	node_mapping = {} # each node and it's leader in the cluster

	for node in data_list: 
		num = node.replace(" ", "")
		node_set.add(num)
		cluster_meta[num] = [num]
		node_mapping[num] = num

	return node_set, cluster_meta, node_mapping

node_set, cluster_meta, node_mapping = readData()

def calculateCloseNeighbors(node):
	close_neighbors = []

	for i in range(24):
		if node[i] == "0": 
			replacement_i = "1"
		elif node[i] == "1":
			replacement_i = "0"
		else: 
			print("SOMETHING IS WRONG")
			raise Exception("the i-th character in the node is neither 0 or 1")

		for j in range(i+1, 24):
			if node[j] == "0": 
				replacement_j = "1"
			elif node[j] == "1":
				replacement_j = "0"
			else: 
				print("SOMETHING IS WRONG")
				raise Exception("the j-th character in the node is neither 0 or 1")

			neighbor = node[0:i]+replacement_i+node[i+1:j]+replacement_j+node[j+1:]

			if neighbor in node_set: 
				close_neighbors.append(neighbor)


		neighbor = node[0:i]+replacement_i+node[i+1:]

		if neighbor in node_set: 
			close_neighbors.append(neighbor)

	return close_neighbors


def mergeClusters(v1, v2): 
	if node_mapping[v1] == node_mapping[v2]: 
		print("THERE IS AN ERROR: the 2 nodes getting merged have the same cluster leader")
		
		raise Exception("The 2 nodes getting merged have the same cluster leader")

	c1_leader = node_mapping[v1] 
	c2_leader = node_mapping[v2]

	c1_nodes = cluster_meta[c1_leader]
	c2_nodes = cluster_meta[c2_leader]

	if len(c1_nodes) < len(c2_nodes): 
		# merge c1 into c2

		# first: assign all nodes in c1 a new leader - the c2 leader
		for n in c1_nodes: 
			node_mapping[n] = c2_leader

		# then combine the elements of the two clusters in the meta table and delete the first one
		c2_nodes += c1_nodes
		cluster_meta[c2_leader] = c2_nodes
		del cluster_meta[c1_leader]
	else: 
		# merge c2 into c1

		# first: assign all nodes in c2 a new leader - the c1 leader
		for n in c2_nodes: 
			node_mapping[n] = c1_leader

		# then combine the elements of the two clusters in the meta table and delete the first one
		c1_nodes += c2_nodes
		cluster_meta[c1_leader] = c1_nodes
		del cluster_meta[c2_leader]

def runClustering():
	count = 0
	for node in node_set: 
		count += 1
		print("at iteration ", count)
		close_neighbors = calculateCloseNeighbors(node)
		
		for neighbor in close_neighbors: 
			if node_mapping[node] == node_mapping[neighbor]:
				next # do nothing	
			else: 
				# if different cluster leaders, then must merge
				mergeClusters(node, neighbor)

			
			# if not, merge


runClustering()
print("the # of clusters remaining are", len(cluster_meta))
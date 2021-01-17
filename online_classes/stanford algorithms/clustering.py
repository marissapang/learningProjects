import pandas as pd
import math

def createSortedData():
	data = pd.read_csv("clustering.txt", header=None)
	data_list = data[0].tolist()
	data_list = data_list[1:]

	edges = [] # list of tuples (tail, head, dist)
	cluster_meta = {} # has map of cluster leader to all items in the cluster
	node_mapping = {} # each node and it's parent in the cluster


	for edge in data_list: 
		tail = int(edge.split(" ")[0])
		head = int(edge.split(" ")[1])
		dist = int(edge.split(" ")[2])	
		edges.append((tail, head, dist))
		cluster_meta[tail] = [tail]
		cluster_meta[head] = [head]
		node_mapping[tail] = tail
		node_mapping[head] = head

	edges.sort(key=lambda x:x[2])
	return edges, cluster_meta, node_mapping
		

edges, cluster_meta, node_mapping = createSortedData()


# edges, cluster_meta, node_mapping = createSortedData()# 

def inSameCluster(v1, v2):
	if node_mapping[v1] == node_mapping[v2]: 
		return True
	else: 
		return False

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


def addEdgeToCluster(edge):
	tail, head, dist = edge

	if inSameCluster(tail, head): 
		print("something is prolly wrong, bc in same cluster is trigger in addEdgeToCluster")
		return
	else: 
		mergeClusters(tail, head)




def runClustering(k):
	for e in edges: 

		if inSameCluster(e[0], e[1]):
			next
		else:
			if len(cluster_meta) == k: 
				print("we are at the end, with only ", k, "clusters now")
				print("the edge with smallest dist remaining is", e)
				return

			addEdgeToCluster(e)

		


runClustering(4)

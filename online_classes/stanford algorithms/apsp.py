import pandas as pd
import numpy as np

def readData(filename):
	data = pd.read_csv(filename, header=None)
	data_list = data[0].tolist()[1:]

	# output = []
	output = {}
	for edge in data_list: 
		edge_list = edge.split(" ")
		tail = int(edge_list[0])-1
		head = int(edge_list[1])-1
		length = int(edge_list[2])

		# output.append((tail, head, length))
		output[(tail, head)] = length

	return output

# g1 = readData("apsp1.txt")
# g2 = readData("apsp2.txt")
g3= readData("apsp3.txt")

n = 1000
# n = 16
# perform APSP for each graph, keep minimum shortest path;
# return NULL if graph has negative cycle

def runFloydWarshall(G): 
	# 3D array of dimenions n (k) * n (i) * n (j)
	A = np.zeros((n, n, n))

	print(G)

	# fill in base case for when k = 0
	print("fill in base case")
	for i in range(n): 
		for j in range(n): 
			if i==j: 
				A[0][i][j] = 0
			elif (i, j) in G: 
				A[0][i][j] = G[(i,j)]
			else: 
				A[0][i][j] = float('inf')

	#print(A)

	# iterate to fill out entire table
	print("iterate over table")
	for k in range(1, n):
		print("k is:", k)
		for i in range(1, n): 
			for j in range(1, n):
				case1 = A[k-1][i][j]
				case2 = A[k-1][i][k] + A[k-1][k][j]
				A[k][i][j] = min(case1, case2)
	#print(A)

	# check for negative cycles
	print("negative cycle check")
	negative_cycle = False
	for i in range(0, n): 
		if A[n-1][i][i] < 0: 
			negative_cycle = True
			break

	if negative_cycle: 
		print("THERE IS A NEGATIVE CYCLE")
		return False

	# check APSP
	print("calculate APSP")
	apsp = float('inf')
	for i in range(0, n): 
		for j in range(0, n): 
			if i != j: 
				apsp = min(apsp, A[n-1][i][j])

	return apsp

answer = runFloydWarshall(g3)
print(answer)




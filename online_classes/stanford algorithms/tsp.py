import pandas as pd
from itertools import combinations

def readData():
	data = pd.read_csv("tsp.txt", header=None)
	data_list = data[0].tolist()[1:]
	num_vertices = len(data_list)

	vertices = []
	v_dict = {}
	v_labels = set()

	count = 0

	for item in data_list: 
		count += 1
		x = float(item.split(" ")[0])
		y = float(item.split(" ")[1])
		vertices.append((x,y))
		v_dict[count] = (x,y)
		v_labels.add(count)

	return vertices, v_dict, v_labels, num_vertices

vertices, v_dict, v_labels, num_vertices = readData()


def calculateDistance(v1, v2):
	x1 = v1[0]
	x2 = v2[0]
	y1 = v1[1]
	y2 = v2[1]

	dist = round(((v1[0]-v2[0])**2 + (v1[1]-v2[1])**2)**(1/2),4)

	return dist
 
def runTSP():
	A = {} # key: (list of vertices, elemet in list that is picked as K), value: the shortest path}
	starting_combination = list(combinations(v_labels, 1))[0]
	for m in range(2, len(vertices)+1):

		# delete all the stuff that is no longer relevant from A
		to_be_deleted = []
		for c, p in A: 
			if len(c) < m - 2: 
				to_be_deleted.append((c,p))

		for key in to_be_deleted: 
			del A[key]

		print("IMPORTANT: starting for loop 1, where m = ", m)

		combination_list = list(combinations(v_labels, m))
		# print("here are the combinations we will cover in this iteration")
		# print(combination_list)
		filtered_combinations = []
		for combination in combination_list: 
			if 1 in combination:
				filtered_combinations.append(combination)

		count = 0
		for combination in filtered_combinations: 
			count += 1

			if count % 50000 == 0:
				print("at combination ", count, " of ", len(filtered_combinations))


			for i in range(len(combination)): 
				point = combination[i]
				# print('point is: ', point)
				prev_combination = combination[:i]+combination[i+1:]
				min_value = float('inf')

				if point != 1:
					# print("...........")
					# print("iterating in point loop, where point = ", point)
					# print("starting_combination is: ", starting_combination) 	
					
					for prev_point in combination: 
						# print("prev_point is: ", prev_point)

						if prev_point != point: 

							if prev_point == 1: 
								if prev_combination == starting_combination: 
									# print("we are in base case: prev_combination == starting_combination")
									new_contender = calculateDistance(v_dict[prev_point], v_dict[point])
								else:
									# print("we are in base case: prev_combination != starting_combination")
									new_contender = float('inf')
								# new_contender += calculateDistance(prev_point, point)
							else:
								new_contender = A[(prev_combination, prev_point)] + calculateDistance(v_dict[prev_point], v_dict[point])
							
							if new_contender < min_value: 
								min_value = new_contender


					A[(combination, point)] = min_value


	# do last step
	print("starting find loop")
	total_min = float('inf')
	for c, p in A: 
		# print("c is: ", c, "and p is", p)
		if c == combination: # this is the final biggest combination
			# print("we are in if statement")
			new_val = A[(c, p)] + calculateDistance(v_dict[p], v_dict[1])
			# print("at this point, total_min is: ", total_min, "and A[c,p] is: ", A[(c,p)])

			
			if new_val < total_min: 
				print("the final p is: ", p)
				total_min = new_val 


	print("*************************")
	print("**********END************")
	print("*************************")
	# total_min += calculateDistance((27166.6667, 9833.3333), (20833.3333,17100.0000)) # dist from last point to first point
	#total_min += calculateDistance((22683.3333, 12716.6667), (23616.6667, 15866.6667)) # dist between point where things split
	print(total_min)

def runTSPOld():
	A = {} # key: (list of vertices, elemet in list that is picked as K), value: the shortest path}
	starting_combination = list(combinations(vertices, 1))[0]
	for m in range(2, len(vertices)+1):
		# print("********************************")
		# print("********************************")
		print("IMPORTANT: starting for loop 1, where m = ", m)

		combination_list = list(combinations(vertices, m))
		# print("here are the combinations we will cover in this iteration")
		# print(combination_list)
		filtered_combinations = []
		for combination in combination_list: 
			if vertices[0] in combination:
				filtered_combinations.append(combination)

		count = 0
		for combination in filtered_combinations: 
			count += 1

			if count % 10000 == 0:
				print("at combination ", count, " of ", len(filtered_combinations))

			# print("--------------------")
			# print("iterating in combination loop, where combination = ", combination)

			for i in range(len(combination)): 
				point = combination[i]
				prev_combination = combination[:i]+combination[i+1:]
				min_value = float('inf')

				if point != vertices[0]:
					# print("...........")
					# print("iterating in point loop, where point = ", point)
					# print("starting_combination is: ", starting_combination) 	
					
					for prev_point in combination: 
						# print("prev_point is: ", prev_point)

						if prev_point != point: 

							if prev_point == vertices[0]: 
								if prev_combination == starting_combination: 
									# print("we are in base case: prev_combination == starting_combination")
									new_contender = calculateDistance(prev_point, point)
								else:
									# print("we are in base case: prev_combination != starting_combination")
									new_contender = float('inf')
								# new_contender += calculateDistance(prev_point, point)
							else:
								new_contender = A[(prev_combination, prev_point)] + calculateDistance(prev_point, point)
							
							if new_contender < min_value: 
								min_value = new_contender


					A[(combination, point)] = min_value


	# do last step
	print("starting find loop")
	total_min = float('inf')
	for c, p in A: 
		# print("c is: ", c, "and p is", p)
		if c == combination: # this is the final biggest combination
			# print("we are in if statement")
			new_val = A[(c, p)] + calculateDistance(p, vertices[0])
			# print("at this point, total_min is: ", total_min, "and A[c,p] is: ", A[(c,p)])

			
			if new_val < total_min: 
				print("the final p is: ", p)
				total_min = new_val 


	print("*************************")
	print("**********END************")
	print("*************************")
	# total_min += calculateDistance((27166.6667, 9833.3333), (20833.3333,17100.0000)) # dist from last point to first point
	#total_min += calculateDistance((22683.3333, 12716.6667), (23616.6667, 15866.6667)) # dist between point where things split
	print(total_min)


runTSP()
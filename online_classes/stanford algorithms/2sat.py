import pandas as pd

filename = "small-2sat.txt"

def readData(filename):
	data = pd.read_csv(filename, header=None)

	data_list = data[0].tolist()[1:]

	variables = set()
	clauses = []

	for line in data_list: 
		c1 = int(line.split(" ")[0])
		c2 = int(line.split(" ")[1])

		variables.add(abs(c1))
		variables.add(abs(c2))

		clauses.append((c1, c2))

	variables_list = list(variables)

	return variables_list, clauses

variables, clauses = readData(filename)
print("VARIABLES")
print(variables)

print("CLAUSES")
print(clauses)
assignments = {}
flipped_variable_list = [] # list of variable, each item represents that variable that has triggered one of the singleBackwardsLoop
local_assignments_list = [] # list of list, each item is a list of all assignments tht were made in the singleBackwardsLoop
def hasContradiction(input_var, input_value):
	if input_var not in assignments: 
		return False # can't have contradiction if not assigned previously
	elif assignments[input_var] == input_value: 
		return False
	elif assignments[input_var] != input_value:
		return True
	else: 
		print("SOMETHING IS WRONG")


def makeAssignment(clause, input_var):
	# input var is a positive number, the one most recently inputed into assignments
	c1 = clause[0]
	c2 = clause[1]

	input_value = assignments[input_var] # True or False

	# if the value we are checking for is not in the clause, then we do nothing
	if not (input_var == abs(c1) or input_var == abs(c2)): 
		return

	# case 1: input corresponds to c1
	if input_var == abs(c1): 
		print("in case 1")
		# 1a: if c1 is true but is negated, then c2 must be true  |OR|  if c1 is false and not negated, then c2 must be truee
		if (input_value == True and c1<0) or (input_value == False and c1>0):
			# c2 must be true
			if not hasContradiction(input_var, input_value): 
				assignments[c2] = True
				return c2
			else: # if there is a contradiction
				return False
				# cancel all the changes in the chain of command
				# flip the original thing back to false and try again. if it still doesn't work.

	# case 2: input corresponds to c2
	elif input_var == abs(c2):
		print(" in case 2")
		# 1a: if c2 is true but is negated, then c1 must be true  |OR|  if c2 is false and not negated, then c1 must be truee
		if (input_value == True and c2<0) or (input_value == False and c2>0):
			# c1 must be true
			if not hasContradiction(input_var, input_value):
				assignments[c1] = True
				return c1
			else:
				return False
	else: 
		print("SOMETHING IS WRONG")


def findNextUnassignedVariable():
	for var in variables: 
		if var not in assignments: 
			return var

def singleBackwardsLoop():
	curr_it_assignments = []
	# assign variable 1 to True
	starting_var = findNextUnassignedVariable()
	assignments[starting_var] = True
	flipped_variable_list.append(starting_var)

	latest_list = [starting_var]

	# condition for while loop: 1) not all variables have assignments, 2) there are no new varialbes getting added
	condition_satisfied = (len(assignments) < len(variables)) and (len(latest_list) > 0)

	# search the list, for anything that contains this, we must do something, and anything that contains negative this
	while condition_satisfied:
		# print("in iteration of while loop, we have made ", len(assignments), "assignments from a list of ", len(variables), "variables")
		print("in iteration of while loop, current, assignments are ", assignments, "and latest_list is", latest_list)
		curr_var = latest_list.pop(0)
		print("curr_var is : ", curr_var)
		for clause in clauses: 
			print("in for loop, at clause ", clause)
			latest_assignment = makeAssignment(clause, curr_var) 
			print("after makeAssignment call, assignments is now: ", assignments)
			if latest_assignment == False: 
				print("latest_assignments is FALSE, so we break the for loop, and flip cndition_satisfied to false loop")
				condition_satisfied = False
				# we found a contradiction
				# we flip the starting variable to false and try again
				assignments.clear()
				assignments[starting_var] = False
				latest_list.clear()
				latest_list = [starting_var]
				break
			elif latest_assignment is not None: 
				latest_list.append(latest_assignment)
				curr_it_assignments.append(latest_assignment)

		if assignments[starting_var] == True: 
			()
			# in this loop we did not yet find a mistake
		else: # run our thing again with false as a start
			# delete all the assignmnets made as part of this iteration
			for var in curr_it_assignments: 
				del assignments[var]

			curr_it_assignments.clear()

			curr_var = latest_list.pop(0)

			# condition for while loop: 1) not all variables have assignments, 2) there are no new varialbes getting added
			condition_satisfied = (len(assignments) < len(variables)) and (len(latest_list) > 0)

			# search the list, for anything that contains this, we must do something, and anything that contains negative this
			while condition_satisfied:
				# print("in iteration of while loop, we have made ", len(assignments), "assignments from a list of ", len(variables), "variables")
				curr_var = latest_list.pop(0)
				for clause in clauses: 
					latest_assignment = makeAssignment(clause, curr_var) 
					if latest_assignment == False: 
						print("latest_assignments is FALSE, so we break the for loop, and flip cndition_satisfied to false loop")
						# we found a contradiction
						# we flip the starting variable to false and try again
						for var in curr_it_assignments: 
							del assignments[var]

						curr_it_assignments.clear()
						return False
					elif latest_assignment is not None: 
						latest_list.append(latest_assignment)
						curr_it_assignments.append(latest_assignment)
					

		condition_satisfied = (len(assignments) < len(variables)) and (len(latest_list) > 0)


	# if we somehow manage to finish the while loop
	print("while loop has ended")
	print("we have made ", len(assignments), "assignments that are all compatible with each other")
	return


def run2SAT():
	while len(assignments) < len(variables):
		print("***********")
		print("in it of run2sat whie loop, len(assignments) is ", len(assignments))
		if len(flipped_variable_list) == 0: 
			print("NOTHING WAS FOUND")
			return 

		result = singleBackwardsLoop()
		if result == False: 
			latest_var = flipped_variable_list.pop()
			del assignments[latest_var]

	print("EVERYTHING WAS ASSIGNED")

run2SAT()



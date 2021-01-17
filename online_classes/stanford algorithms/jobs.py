import pandas as pd
import math


jobs_list = []

def processData():
	data = pd.read_csv("jobs.txt")
	data_list = data['10000'].tolist()

	for job in data_list: 
		weight = int(job.split(" ")[0])
		length = int(job.split(" ")[1])
		difference = weight - length
		ratio = weight / length
		jobs_list.append((weight, length, difference, ratio))

def sortJobsList():
	sorted_list = sorted(jobs_list, key=lambda element: (element[2], element[0]))
	# sorted_list = sorted(jobs_list, key=lambda element: (element[3]))
	sorted_list.reverse()

	return sorted_list


def mainFunction(): 
	processData()
	sorted_list = sortJobsList()

	completion_time= 0
	sum_weighted_completion_time = 0



	for job in sorted_list: 
		weight = job[0]
		length = job[1]

		completion_time += length
		sum_weighted_completion_time += completion_time * weight

		print(sum_weighted_completion_time)


mainFunction()



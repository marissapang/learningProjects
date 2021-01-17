import pandas as pd

def readData():
	data = pd.read_csv("mwis.txt", header=None)
	data_list = data[0].tolist()
	data_list = data_list[1:]
	print(data_list[0:10])
	return data_list

V = readData()

def runMWIS():
	weight_tracking = []
	mwis_tracking= [] # list of list

	# for n = 0
	weight_tracking.append(V[0])
	mwis_tracking.append([0])

	# for n = 1
	if V[0] >= V[1]: 
		weight_tracking.append(V[0])
		mwis_tracking.append([0])
	else:
		weight_tracking.append(V[1])
		mwis_tracking.append([1])

	# for n >= 2
	for i in range(2, len(V)):
		g_prime = weight_tracking[i-1]
		g_2prime = weight_tracking[i-2]+V[i]


		if g_prime >= g_2prime: 
			weight_tracking.append(g_prime)
			mwis_tracking.append(mwis_tracking[i-1])
		else: 
			weight_tracking.append(g_2prime)
			mwis_tracking.append(mwis_tracking[i-2]+[i])

	return mwis_tracking[-1]



x = runMWIS()

def searchForIndices(result):
	input_list = [1, 2, 3, 4, 17, 117, 517, 997]
	output = ""

	for num in input_list: 
		if num-1 in result:
			output+="1"
		else: 
			output+="0"

	print(output)

searchForIndices(x)



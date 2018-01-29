import numpy as np 
import operator
import sys

# Only shows the affinity for the top K clusters
topK = int(sys.argv[1])

selectedCluster = int(sys.argv[2])

# Determines how many edges get removed.
EDGE_THRESHOLD = 0.1

matrix = np.loadtxt("output_B_MLE.txt")

rows = matrix.shape[0]
cols = matrix.shape[0]

curCol = 1

jsonFile = open("YelpAffinity.json", "w+")
jsonFile.write('{\n"links": [\n')

# The number of lines to be written in the json file.
numLines = topK * 2

topKMap = {}

# for row in range(0, rows):
# 	for col in range(curCol, cols):
# 		topKMap[col] = matrix[row][col]

# 	sorted_topK = sorted(topKMap.items(), key=operator.itemgetter(1), reverse = True)

# 	for item in sorted_topK[:topK]:
# 		topKCol = int(item[0])

# 		if matrix[row][topKCol] != 0:
# 			numLines += 1

# 	topKMap.clear()
# 	curCol += 1

# for row in range(0, rows):
# 	for col in range(0, cols):
# 		# Each group has perfect affinity for itself
# 		if row != col:
# 			topKMap[col] = matrix[row][col]


# 	sorted_topK = sorted(topKMap.items(), key=operator.itemgetter(1), reverse = True)

# 	for item in sorted_topK[:topK]:
# 		topKCol = int(item[0])

# 		if matrix[row][topKCol] != 0:
# 			numLines += 1

# 	topKMap.clear()

# curCol = 1
# count = 0
# topKMap.clear()


affinityDescriptionString = ""

count = 0

for row in range(0, rows):
	for col in range(0, cols):

		# Each group has perfect affinity for itself
		if row != col:
			topKMap[col] = matrix[row][col]

	sorted_bottomK = sorted(topKMap.items(), key=operator.itemgetter(1))
	sorted_topK = sorted(topKMap.items(), key=operator.itemgetter(1), reverse = True)

	# Select top k affinity clusters
	for item in sorted_topK[:topK]:
		topKCol = int(item[0])

		if row == selectedCluster:

			affinityDescriptionString += "Cluster " + str(topKCol) + ": " + str(matrix[row][topKCol]) + ", "

			count += 1
			if count == numLines:
				jsonFile.write('{"source":' + '"' + str(row) + '","target":' + '"' + str(topKCol) + '","affinity":' + str(matrix[row][topKCol]) + '}\n')
			else:
				jsonFile.write('{"source":' + '"' + str(row) + '","target":' + '"' + str(topKCol) + '","affinity":' + str(matrix[row][topKCol]) + '},\n')

	# Select bottom k affinity clusters
	for item in sorted_bottomK[:topK]:
		topKCol = int(item[0])

		if row == selectedCluster:

			affinityDescriptionString += "Cluster " + str(topKCol) + ": " + str(matrix[row][topKCol]) + ", "

			count += 1
			if count == numLines:
				jsonFile.write('{"source":' + '"' + str(row) + '","target":' + '"' + str(topKCol) + '","affinity":' + str(matrix[row][topKCol]) + '}\n')
			else:
				jsonFile.write('{"source":' + '"' + str(row) + '","target":' + '"' + str(topKCol) + '","affinity":' + str(matrix[row][topKCol]) + '},\n')


	topKMap.clear()	
	curCol += 1

jsonFile.write(']\n}')
jsonFile.close()
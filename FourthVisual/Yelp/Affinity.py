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

affinityDescriptionString = ""

count = 0

for col in range(0, cols):

	if selectedCluster != col:
		topKMap[col] = matrix[selectedCluster][col]

	sorted_bottomK = sorted(topKMap.items(), key=operator.itemgetter(1))
	sorted_topK = sorted(topKMap.items(), key=operator.itemgetter(1), reverse = True)

for item in sorted_topK[:topK]:
	topKCol = int(item[0])

	affinityDescriptionString += "Cluster " + str(topKCol) + ": " + str(matrix[selectedCluster][topKCol]) + ", "

	count += 1
	if count == numLines:
		jsonFile.write('{"source":' + '"' + str(selectedCluster) + '","target":' + '"' + str(topKCol) + '","affinity":' + str(matrix[selectedCluster][topKCol]) + '}\n')
	else:
		jsonFile.write('{"source":' + '"' + str(selectedCluster) + '","target":' + '"' + str(topKCol) + '","affinity":' + str(matrix[selectedCluster][topKCol]) + '},\n')


bottomKIndex = 0

tracker = 0

while tracker < topK:

	if (sorted_bottomK[bottomKIndex] in sorted_topK[:topK]) == False:

		topKCol = int(sorted_bottomK[bottomKIndex][0])

		affinityDescriptionString += "Cluster " + str(topKCol) + ": " + str(matrix[selectedCluster][topKCol]) + ", "

		count += 1
		if count == numLines:
			jsonFile.write('{"source":' + '"' + str(selectedCluster) + '","target":' + '"' + str(topKCol) + '","affinity":' + str(matrix[selectedCluster][topKCol]) + '}\n')
		else:
			jsonFile.write('{"source":' + '"' + str(selectedCluster) + '","target":' + '"' + str(topKCol) + '","affinity":' + str(matrix[selectedCluster][topKCol]) + '},\n')

		tracker += 1

	bottomKIndex += 1

jsonFile.write(']\n}')
jsonFile.close()
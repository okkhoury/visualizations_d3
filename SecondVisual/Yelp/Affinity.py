import numpy as np 

matrix = np.loadtxt("output_B_MLE.txt")

rows = matrix.shape[0]
cols = matrix.shape[0]

curCol = 1

jsonFile = open("YelpAffinity.json", "w+")
jsonFile.write('{\n"links": [\n')

numLines = 0

for row in range(0, rows):
	for col in range(curCol, cols):

		if matrix[row][col] != 0:
			numLines += 2

	curCol += 1

curCol = 1
count = 0

for row in range(0, rows):
	for col in range(curCol, cols):

		if matrix[row][col] > .1:
			count += 2
			if count == numLines:
				jsonFile.write('{"source":' + '"' + str(row) + '","target":' + '"' + str(col) + '","affinity":' + str(matrix[row][col]) + '},\n')
				jsonFile.write('{"source":' + '"' + str(col) + '","target":' + '"' + str(row) + '","affinity":' + str(matrix[row][col]) + '}\n')
			else:
				jsonFile.write('{"source":' + '"' + str(row) + '","target":' + '"' + str(col) + '","affinity":' + str(matrix[row][col]) + '},\n')
				jsonFile.write('{"source":' + '"' + str(col) + '","target":' + '"' + str(row) + '","affinity":' + str(matrix[row][col]) + '},\n')

			
	curCol += 1

jsonFile.write(']\n}')
jsonFile.close()
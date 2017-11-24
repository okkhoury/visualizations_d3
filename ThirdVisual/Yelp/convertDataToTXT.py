import itertools
import re
import json
import os.path
import math
import random

users = []

colorFile = open("NodeColorMap.txt", "w+")
colorFile.write('var colorMap = {\n')

def createJsonFile(i):
	dataFile = "print_cluster_" + i + ".txt"

	jsonFileName = "indvCluster" + i + ".json"

	jsonFile = open(jsonFileName, "w+")
	jsonFile.write('{\n"links": [\n')

	if (os.path.isfile(dataFile)):
		numLines = 0
		with open(dataFile) as file:
			for line in file:
				numLines += 1

		count = 0
		with open(dataFile) as file:

			for line in file:
				ui = line[3:25]
				uj = line[29:51]

				if ui not in users:
					users.append(ui)
					colorFile.write('\t' + '"' + ui + '"' + ':' + '"rgb(' + str(int((math.floor(random.randint(0,255))))) + ',' + str(int((math.floor(random.randint(0,255))))) + ',' + str(int((math.floor(random.randint(0,255))))) + ')",\n')

				# if uj not in users:
				# 	users.append(uj)
				# 	colorFile.write('\t' + '"' + uj + '"' + ':' + '"rgb(' + str(int((math.floor(random.randint(0,255))))) + ',' + str(int((math.floor(random.randint(0,255))))) + ',' + str(int((math.floor(random.randint(0,255))))) + ')",\n')

				count += 1

				if count == numLines:
					jsonFile.write('{"source":' + '"' + ui + '","target":' + '"' + uj + '"}\n')
				else:
					jsonFile.write('{"source":' + '"' + ui + '","target":' + '"' + uj + '"},\n')

		jsonFile.write(']\n}')
		jsonFile.close()


for i in range(0, 31):
	createJsonFile(str(i))

colorFile.write('}')
colorFile.close()







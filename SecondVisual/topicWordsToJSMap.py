import itertools
import re
import json

wordMapFile = open("WordMap.txt", "w+")
wordMapFile.write('var wordMap = {\n')

with open("TopicWords.txt", "r") as file:
	for line in file:
		group = line[0:2].strip()
		words = ""

		if len(group) == 1:
			words = line[1:].strip()
		else:
			words = line[2:].strip()

		wordStr = ""
		count = 1
		for word in re.split(r'\t+', words)[0:10]:

			if count == 10:
				wordStr += word
			else:
				wordStr += word + ', '

			count += 1

		wordMapFile.write('\t"' + group + '":' + '"' + wordStr + '",\n')

wordMapFile.write('}')

		

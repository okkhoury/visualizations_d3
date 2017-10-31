# import itertools
# import re
# import json

# userToGroup = {}

# users = []

# userToIndex = {}

# def mapGroupsToUsers():
# 	with open("UserMembership.txt", "r") as file:

# 		index = 0

# 		for line1, line2 in itertools.izip_longest(file, file, fillvalue=''):

# 			userID = line1.strip()

# 			users.append(userID)

# 			# Format each users clusters into a list of values
# 			clusters = re.split(r'\t+', line2)
# 			clusters = clusters[:-1]

# 			maxSum = 0
# 			majorGroup = 0

# 			for cluster in clusters:
# 				numsInCluster = re.findall(r'\d+', cluster)

# 				majorSum = int(numsInCluster[1]) + int(numsInCluster[2])

# 				if majorSum > maxSum:
# 					majorGroup = int(numsInCluster[0])

# 				maxSum = max(maxSum, majorSum)

# 			userToGroup[userID] = majorGroup
# 			userToIndex[userID] = index
# 			index += 1

# def getFriendEdges():

# 	count = 0
# 	with open("yelpFriends_1000.txt") as file:
# 		for line in file:
			
# 			friends = re.split(r'\t+', line)
# 			user = friends[0].strip()

# 			# Don't include the current user in the list of his friends
# 			friends = friends[1:]

# 			listOfFriends = []

# 			for friend in friends:
# 				if friend in users and user in userToGroup and user in users:
# 					jsonFile.write('{"source":' + '"' + user + '"' + ',"target":' + '"' + friend + '"' + ',"group":' +  str(userToGroup[user]) + '},\n')


# jsonFile = open("data.json", "w+")
# jsonFile.write('{\n"links": [\n')

# mapGroupsToUsers();
# getFriendEdges();

# jsonFile.write(']\n}')
# jsonFile.close()




# ### Individual Cluster Plot. Generate Json

# import itertools
# import re
# import json

# def createJsonFile(i):
# 	dataFile = "print_cluster_" + i + ".txt"

# 	jsonFileName = "indvCluster" + i + ".json"

# 	jsonFile = open(jsonFileName, "w+")
# 	jsonFile.write('{\n"links": [\n')

# 	numLines = 0
# 	with open(dataFile, "a+") as file:
# 		for line in file:
# 			numLines += 1

# 	count = 0
# 	with open(dataFile) as file:

# 		for line in file:
# 			ui = line[3:25]
# 			uj = line[29:51]

# 			count += 1

# 			if count == numLines:
# 				jsonFile.write('{"source":' + '"' + ui + '","target":' + '"' + uj + '"}\n')
# 			else:
# 				jsonFile.write('{"source":' + '"' + ui + '","target":' + '"' + uj + '"},\n')

# 	jsonFile.write(']\n}')
# 	jsonFile.close()

# for i in range(0, 31):
# 	createJsonFile(str(i))


### MISERABLES.JSON

import itertools
import re
import json

userToGroup = {}

users = []

userToIndex = {}

def mapGroupsToUsers():
	with open("UserMembership.txt", "r") as file:

		index = 0

		for line1, line2 in itertools.izip_longest(file, file, fillvalue=''):

			userID = line1.strip()

			users.append(userID)

			# Format each users clusters into a list of values
			clusters = re.split(r'\t+', line2)
			clusters = clusters[:-1]

			maxSum = 0
			majorGroup = 0

			for cluster in clusters:
				numsInCluster = re.findall(r'\d+', cluster)

				majorSum = int(numsInCluster[1]) + int(numsInCluster[2])

				if majorSum > maxSum:
					majorGroup = int(numsInCluster[0])

				maxSum = max(maxSum, majorSum)

			userToGroup[userID] = majorGroup
			userToIndex[userID] = index
			index += 1

def getFriendEdges():
	with open("yelpFriends_1000.txt") as file:
		for line in file:
			
			friends = re.split(r'\t+', line)
			user = friends[0].strip()

			# Don't include the current user in the list of his friends
			friends = friends[1:]

			listOfFriends = []

			for friend in friends:
				if friend in users and user in users:
					listOfFriends.append(friend)

			if listOfFriends:
				jsonFile.write('{"name":' + '"' + user + '"' + ',"size":1000,"imports":' + json.dumps(listOfFriends).replace(" ", "") +'},\n')



jsonFile = open("hiveplot.json", "w+")
jsonFile.write('[\n')
mapGroupsToUsers();
getFriendEdges();
jsonFile.write(']')

jsonFile.close()




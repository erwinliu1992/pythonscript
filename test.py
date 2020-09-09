import re
import os

def getNum(string):
	pattern = re.compile('\d+')
	nums_list = pattern.findall(string)
	return nums_list

def getLineFromFile(readfile):
	rf = open(readfile)
	lines = rf.readlines()
	for line in lines:
		nums_list = getNum(line)
		for num in nums_list[1:]:
			sql = "insert " + nums_list[0] + "-- " + num
			print(sql)



getLineFromFile("txt")




from bs4 import BeautifulSoup
import requests


 
dataSource = requests.get('https://www.youtube.com/playlist?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH').text


dataSoup = BeautifulSoup(dataSource, 'lxml')
data = dataSoup.find_all(class_='timestamp')

 
 
hourList =[]
minList=[]
secondList=[]

totalHour = []
totalMin = []
totalSec = []


def makeCountList(data): 
	for item in data:
		splitItem = item.text.split(':')
		if len(splitItem) == 3:
			hourList.append(splitItem[0])
			minList.append(splitItem[1])
			secondList.append(splitItem[2])
		if len(splitItem) == 2:
			minList.append(splitItem[0])
			secondList.append(splitItem[1])

makeCountList(data)

def secondToMin(num):
	min = int(str(num / 60).split('.')[0])
	sec = num - (min*60)
	totalMin.append(min)
	totalSec.append(sec)

def minToHour(num):
	hour = int(str(num / 60).split('.')[0])
	min = num - (hour*60)
	totalHour.append(hour)
	totalMin.append(min)
 
sumSecond = 0
for item in secondList:
	sumSecond += int(item)
secondToMin(sumSecond)


sumMin = 0
for item in minList:
	sumMin += int(item)
minToHour(sumMin)

sumHour = 0
for item in hourList:
	sumHour += int(item)
totalHour.append(sumHour)


def finalOutput(hourList, minList, secList):
	totalHour = 0
	totalMinute = 0
	totalSecond = 0
	for item in hourList:
		totalHour += item
	for item in minList:
		totalMinute += item
	for item in secList:
		totalSecond += item
	print(f'The total video time for this flask series is {totalHour} hour, {totalMinute} min, {totalSecond} second')

finalOutput(totalHour, totalMin, totalSec)
	
	


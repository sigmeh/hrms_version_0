#!/usr/bin/env python
import matplotlib; matplotlib.use('Agg') 
import numpy as np; import pylab as pl; print
from pylab import rcParams
import cgi,json,os,sys
rcParams['figure.figsize'] = 28,22
def save(saveName, saveContents):
	saveName = path + '/' + saveName
	saveFile = ''
	for i in range(len(saveContents)):
		saveFile += str(saveContents[i]) + ' '
	open(saveName, 'w').write(saveFile)
data = cgi.FieldStorage()['package'].value
data = json.loads(data)
filename = data[0]
threshold = data[1]
if not os.path.exists(filename):		#handle filenames that don't exist
	print 'File not formatted or file does not exist'
	sys.exit()
#if not type(threshold) is int or threshold < 1 or threshold > 400:
#	print 'Enter valid threshold as integer'
#	sys.exit()
path = filename.split('.')[0]	#derive filename to retrieve formatted data
datapath = path + '/' + path + '_data.csv'
with open(datapath,'r') as f:
	data = f.read()
dataArray = data.split()
points = []
for i in range(0,len(dataArray),2):		#add number pairs to array points[]
	point = []
	point.append(float(dataArray[i]))
	point.append(int(float(dataArray[i+1])))
	points.append(point)
peaks = [] 								#collected peak data (all peaks)
peak = []								#temp data for each peak
onPeak = False
if points[0][1] > 0:
	onPeak = True
else:
	onPeak = False
for i in range(len(points)):
	if points[i][1] > 0:				#add point to peak[] if it has intensity
		onPeak = True
		peak.append(points[i])
	else:
		if (onPeak):					#arrived at first zero after peak
			peaks.append(peak)			#add new peak to peaks[]
			onPeak = False
		peak = []						#reset temp peak holder
save('peaks.txt',peaks)
maxPeaks = []							#create array of peak maxima (one point for each peak)
for i in range(len(peaks)):				#iterate over all peaks
	max = [0,0]
	for j in range(len(peaks[i])):		#iterate over points within each peak
		if float(peaks[i][j][1]) > max[1]:
			max = peaks[i][j]
	maxPeaks.append(max)				#add maximum intensity for each peak to maxPeaks[]
maxPeakSort = sorted(maxPeaks, key=lambda intensity: intensity[1])
maxPeakSort.reverse()			#sort by intensity
save('maxPeaks.txt',maxPeaks)

def checkPeak(origin, newLimit, direction):
	for i in range(origin, newLimit, direction):
		val = abs(maxPeaksTrunc[i][0] - maxPeaksTrunc[origin][0])
		if val > .99 and val < 1.01:
			return i		#return index value of relevant point
	return False			#return False if no relevant point is found

def checkNearbyPeaks(loc):
	candidateLines = [maxPeaksTrunc[loc]]	
	positions = [loc]
	num = loc
	for i in range(loc, len(maxPeaksTrunc)):		#find testable range for new peak
		if maxPeaksTrunc[i][0] - maxPeaksTrunc[loc][0] > 1.01:
			num = i
			break
	newLimit = checkPeak(loc,num,1)
	if newLimit:		#found relevant new point
		candidateLines.append(maxPeaksTrunc[newLimit])
		positions.append(newLimit)
		for i in range(newLimit,len(maxPeaks)):
			if maxPeaksTrunc[i][0] - maxPeaksTrunc[newLimit][0] > 1.01:
				num = i
				break	
		newLimit = checkPeak(newLimit,num,1)
		if newLimit:
			candidateLines.append(maxPeaksTrunc[newLimit])
			positions.append(newLimit)
			for i in range(loc, 0, -1):
				if abs(maxPeaksTrunc[i][0] - maxPeaksTrunc[loc][0]) > 1.01:
					num = i
					break
			newLimit = checkPeak(loc, num,-1)
			if newLimit:
				candidateLines.append(maxPeaksTrunc[newLimit])
				positions.append(newLimit)
				for i in range(newLimit, 0, -1):
					if abs(maxPeaksTrunc[i][0] - maxPeaksTrunc[newLimit][0]) > 1.01:
						num = i
						break
				newLimit = checkPeak(newLimit, num,-1)
				if newLimit:
					candidateLines.append(maxPeaksTrunc[newLimit])
					positions.append(newLimit)
					return candidateLines
	return candidateLines			#test failed (peak is not a candidate for ruthenium)

RuCount = 0									#count number of ruthenium species
RuList = []
maxPeaksTrunc = maxPeaks
maxPeakSortTrunc = maxPeakSort				#new array for truncating line data

while len(maxPeakSortTrunc) > 1:	
	testPeak = maxPeakSortTrunc[0]
	checknum = maxPeaksTrunc.index(testPeak)
	candidateLines = checkNearbyPeaks(checknum)
	if len(candidateLines) == 5:			#found ruthenium species
		RuCount += 1
		RuList.append(candidateLines)
	for i in range(len(candidateLines)):
		maxPeakSortTrunc.pop(maxPeakSortTrunc.index(candidateLines[i]))	#truncate list
		maxPeaksTrunc.pop(maxPeaksTrunc.index(candidateLines[i]))		#truncate list			
				
columns = round(RuCount**0.5)						
rows = columns + 1
f1 = pl.figure(1)
for i in range(int(rows*columns)):				#create figure containing subplots for each Ru candidate
	if i < len(RuList):					
		xmin = int(RuList[i][0][0]) - 12			#find "arbitrary" xmin value for plotting
		for j in range(0, len(points)):
			if points[j][0] > xmin:
				xmin = j
				break
		xmax = int(RuList[i][0][0]) + 12
		for j in range(xmin, len(points)):
			if points[j][0] > xmax:
				xmax = j
				break
		subplotX = []; subplotY = []
		for j in range(xmin, xmax):
			subplotX.append(points[j][0])
			subplotY.append(points[j][1])

		pl.subplot(rows,columns,i+1).plot(subplotX, subplotY)
		pl.subplot(rows,columns,i+1).xlabel = ''
		pl.subplot(rows,columns,i+1).ylabel = ''
		

figurename = 'RuCandidates'
matplotlib.pyplot.savefig(path + '/' + path + '_' + figurename + '.png')

RuCandidatesHtml = """\
<head></head>
<body>
	<div id='title'>""" + path + '_' + figurename + """ </div>
	
	<img src='""" + path + '_' + figurename + """.png'/>
	<style>
		#title{
			font-size:30px;
		}
		img{
			width:80%;
			margin:0px;
			
		}
	</style>
</body>
"""
open(path + '/' + path + '_' + figurename+ '.html','w').write(RuCandidatesHtml)

#print 'File'
#print str(len(maxPeakSort))


#print 'File saved... no data to print'	
#save('maxPeaks.txt', maxPeaks)
#print json.dumps(RuList)
print RuList
'''		
print 'Done.....'
print "Number of Ruthenium candidates: %s" %RuCount	
'''
'''	
truncatedData = []
peakString = ''
for i in range(len(peaks)):
	peakString += str(peaks[i]) + ' '
open('peaks.txt','w').write(peakString)
print 'File saved... no data to print'
'''	
	
'''	
intensity = sorted(points, key=lambda intensity: intensity[1])
intensity.reverse()
intensityString=''
for i in range(len(intensity)):
	intensityString = intensityString + ' ' + str(intensity[i])
open('scratch.txt','w').write(intensityString)

'''
	
	
	
	
	
#print json.dumps(intensity)




#print len(dataArray)
#print json.dumps(dataArray)




'''
xPath = path + '_xVals.txt'
yPath = path + '_yValsNorm.txt'
with open(xPath,'r') as f:
	xData = f.read()			#read x values from formatted data
xArray = xData.split()
with open(yPath,'r') as f:		#read y values from normalized data
	yData = f.read()
yArray = yData.split()
xArrayNum = []; yArrayNum = []
for i in range(len(xArray)):
	pair = []
	xArrayNum.append(float(xArray[i]))	#x values loaded as float
	yArrayNum.append(int(yArray[i]))	#y values loaded as int
intensityHighToLow = []
'''
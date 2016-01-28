#!/usr/bin/env python
import cgi,json,os
import matplotlib; matplotlib.use('Agg') 
import numpy as np; import pylab as pl; print
from pylab import rcParams
rcParams['figure.figsize'] = 8,3
def findLocation(number):
	for i in range(len(xArrayNum)):
		if (xArrayNum[i] >= number):
			return i		#return array location for target number
#start program
data = cgi.FieldStorage()['spectralData'].value
spectralData = json.loads(data)
filename = spectralData[0]
if not os.path.exists(filename):
	print 'File not formatted or file does not exist'
else:
	
	path = filename.split('.')[0]	#derive filename
	path = path + '/' + path
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
		xArrayNum.append(float(xArray[i]))
		yArrayNum.append(int(yArray[i]))
	
	if spectralData[2] != 'full':
		xmin = int(spectralData[1])
		xmax = int(spectralData[2])
		xminLocation = findLocation(xmin)
		xmaxLocation = findLocation(xmax)
	else:
		#spectralData[2] = len(xArray)
		xminLocation = 0
		xmaxLocation = len(xArray)
		#xmin = int(spectralData[1])
		#xmax = int(spectralData[2])
	
	pl.plot(xArrayNum, yArrayNum)			#plot data
	pl.title('DESI HRMS spectrum')
	pl.xlabel('m/z')
	pl.ylabel('intensity')
	
	xmin = round(xArrayNum[xminLocation])
	xmax = round(xArrayNum[xmaxLocation-1])
	
	pl.xlim(xmin, xmax)
	ymin = 0; ymax = spectralData[4]
	pl.ylim(ymin, ymax)
	fignum = str(1)
	pl.tight_layout()
	savedFilePath = path + '_fig_full.png'
	#savedFilePath = path + '_fig' + fignum + '.png'
	matplotlib.pyplot.savefig(savedFilePath)		#save file for transfer to html
	spectralData[0] = savedFilePath
	spectralData[1] = xmin
	spectralData[2] = xmax
	spectralData[3] = ymin
	spectralData[4] = ymax
	spectralData[5] = xmaxLocation - xminLocation
	
	#print savedFilePath
	print json.dumps(spectralData)
		
		
'''		
		pair = []
		pair.append(xArray[i])
		pair.append(yArray[i])
		pairs.append(pair)
	#xArrayNum = []; yArrayNum = []
'''
	
		
		
		
'''
		for i in range(len(xArray)):	#create (x,y) point pairs 
			pair = []
			pair.append(xArray[i])
			pair.append(yArray[i])
			pairs.append(pair)
		xArrayNum = []; yArrayNum = []
		for i in range(0,len(xArray),1):		#convert data array to numbers
			xArrayNum.append(float(xArray[i]))
			yArrayNum.append(int(yArray[i]))
		pl.plot(xArrayNum, yArrayNum)			#plot data
		pl.title('DESI HRMS spectrum')
		pl.xlabel('m/z')
		pl.ylabel('intensity')
		xmin = round(xArrayNum[0])
		xmax = round(xArrayNum[len(xArrayNum)-1])
		pl.xlim(xmin, xmax)
		ymin = 0; ymax = 100
		pl.ylim(ymin, ymax)
		fignum = str(1)
		pl.tight_layout()
		savedFilePath = path + '_fig_full.png'
		#savedFilePath = path + '_fig' + fignum + '.png'
		matplotlib.pyplot.savefig(savedFilePath)		#save file for transfer to html
		dataArray = []
		dataArray.append(savedFilePath)
		dataArray.append(xmin)
		dataArray.append(xmax)
		dataArray.append(ymin)
		dataArray.append(ymax)
		dataArray.append(len(xArrayNum))
		#print savedFilePath
		print json.dumps(dataArray)
'''
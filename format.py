#!/usr/bin/env python
import cgi,os
print

def formatData(lines):					#create folder; separate header from data; save files
	foldername = filename[:len(filename)-4]
	os.makedirs(foldername)
	header = lines.split()[:26]			#extract header
	head = ''
	for word in header:
		head += word
	head = head.replace(',',',\r',8)	#reformat header text for saving
	headname = foldername + '_head.txt'
	open(foldername + '/' + headname,'w').write(head)	#save header file
	body = lines.split()[26:] 			#extract body (x/y pairs)
	for i in range(len(body)):
		body[i] = body[i].replace(',',' ')	#format data for saving
	xVals = []; yVals = []
	for i in range(len(body)):
		temp = body[i].split()
		xVals.append(float(temp[0]))		#create array of x values (float)
		yVals.append(int(float(temp[1])))	#create array of y values (int)
	xFormatted = ''; yFormatted = '';
	for i in range(len(xVals)):
		xFormatted += str(xVals[i]) + ' '	#convert x array to string
		yFormatted += str(yVals[i]) + ' '	#convert y array to string
	xname = foldername + '_xVals.txt' 
	yname = foldername + '_yVals.txt'
	open(foldername + '/' + xname,'w').write(xFormatted)	#save x values
	open(foldername + '/' + yname, 'w').write(yFormatted)	#save y values
	maxY = 0; xAtMaxY = 0
	for i in range(len(yVals)):			#find maxY value for normalization
		if yVals[i] > maxY:
			maxY = yVals[i]
			xAtMaxY = i
	massAtMaxY = xVals[xAtMaxY]
	yNormalized = []
	for i in range(len(yVals)):			#normalize y values
		y = yVals[i] * 400 / maxY		#normalized to 400!
		yNormalized.append(y)
	yNormVals = ''
	for i in range(len(yNormalized)):	#convert normalized y values to string
		yNormVals += str(yNormalized[i]) + ' '
	yNorm = foldername + '_yValsNorm.txt'
	open(foldername + '/' + yNorm,'w').write(yNormVals)
	data = ''
	for word in body:
		data += word + '\n'				#format for saving
	dataname = foldername + '_data.csv'
	open(foldername + '/' + dataname,'w').writelines(data)	#make data file
	originalFile = foldername + '_original.csv'
	open(foldername + '/' + originalFile,'w').writelines(lines)	#place original data in new folder
	print; print "Folder \'%s\' was created. Folder \'%s\' contains:<br>" %(foldername, foldername)
	print "&nbsp&nbsp %s <br>" %headname
	print "&nbsp&nbsp %s <br>" %dataname
	print "&nbsp&nbsp %s <br>" %xname
	print "&nbsp&nbsp %s <br>" %yname
	print "&nbsp&nbsp %s <br>" %yNorm
	print "&nbsp&nbsp %s <br>" %originalFile
	#print "The maximum intensity (%s), which occurs at data point %s (m/z = %s), has been normalized to 400." %(maxY,xAtMaxY,massAtMaxY)
	return body
#start program
filename = cgi.FieldStorage()['package'].value	#get filename
if not os.path.exists(filename):				#if file does not exist
	print "\'%s\' does not exist" %filename
else:
	folder = filename.rsplit('.')
	if os.path.exists(folder[0]):				#check for previously-formatted data
		print "\'%s\' is formatted" %filename
	else:										#data is new; format data
		with open(filename) as f:	
			lines = f.read()
		data = formatData(lines)
	

	
	

	
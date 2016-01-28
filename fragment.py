#!/usr/bin/env python
import cgi, json; print
fragPack = cgi.FieldStorage()['fragPack'].value
data = json.loads(fragPack)
massesToTest = data[0]
peak = massesToTest[0][0]
fragmentsToTest = data[1]
#print fragmentsToTest
'''
fragName = data[1]
splitter = data[0].split()
atom = []; number = []
entries = {}
for i in range(0,len(splitter),2):
	atom.append(splitter[i])
	number.append(splitter[i+1])
'''
with open('massData.txt','r') as f:	#load mass data from file
	doc = f.read()
datalines = doc.split('\r')
massData=[]
for i in range(len(datalines)):
	splitline = datalines[i].split()
	massData.append(splitline)	
mass = {}						#parse mass data for use
for i in range(len(massData)):
	massData[i][3] = massData[i][3].split('#')[0]	#get rid of trailing hash
	if float(massData[i][5]) > 30:	
		mass[massData[i][2]] = massData[i][3]

fragments = {
'Ru': 'Ru 1',
'PhIOPiv2': 'C 16 H 23 O 4 I 1',
'OPiv': 'C 5 H 9 O 2',
'HOPiv': 'C 5 H 10 O 2',
'Na': 'Na 1',
'H2O': 'H 2 O 1',
'O': 'O 1',
'H': 'H 1',
'OH': 'O 1 H 1',
'OAc': 'C 2 H 3 O 2',
'HOAc': 'C 2 H 4 O 2',
'esp': 'C 16 H 20 O 4',
'espH': 'C 16 H 21 O 4',
'espH2': 'C 16 H 22 O 4',
'Cl': 'Cl 1',
'TcesNH2': 'C 2 H 4 S 1 O 3 N 1 Cl 3',
'TcesNH': 'C 2 H 3 S 1 O 3 N 1 Cl 3',
'TcesN': 'C 2 H 2 S 1 O 3 N 1 Cl 3'
}

fragMass = {}; moleculeMass = 0	#fragMass dictionary contains exact mass for each fragment
for i in fragments:
	moleculeMass = 0
	formula = fragments[i].split()
	for j in range(0, len(formula), 2):
		atom = formula[j]
		number = int(formula[j+1])
		atomsMass = float(mass[atom]) * number
		moleculeMass += atomsMass
	fragMass.update({i:moleculeMass})
'''
massesToTest = data[0]
peak = massesToTest[0][0]
fragmentsToTest = data[1]
'''
#print fragmentsToTest
formulaArray = []
mass = peak
#print fragMass['Ru']
'''
if 'Ru' in fragmentsToTest:
	highnum = mass/fragMass[fragments['Ru']]
	for i in range
'''


def getMass(formulaArray):
	mass = peak
	for i in range(len(formulaArray)):
		mass -= fragMass[formulaArray[i][0]]*formulaArray[i][1]
	if abs(mass) < 0.01 or abs(abs(mass) - 1) < 0.01:
		#print abs(mass) - 1
		print "-----------------Candidate: " + str(formulaArray) + 'endAppend'
	return mass

for i in range(len(fragmentsToTest)):
	formulaArray.append([fragmentsToTest[i],0])
print formulaArray
counter = 0
highnum = int(mass/fragMass[fragmentsToTest[0]]) + 2
for i in range(0, highnum):
	formulaArray[0] = [fragmentsToTest[0],i]
	for j in range(1,len(formulaArray)):
		formulaArray[j][1] = 0
	mass = getMass(formulaArray)
	print str(formulaArray) +  '; mass: ' + str(mass)
	if len(fragmentsToTest) > 1:									# new loop conditional
		highnum = int(mass/fragMass[fragmentsToTest[1]]) + 2
		for j in range(0, highnum):
			formulaArray[1] = [fragmentsToTest[1],j]
			mass = getMass(formulaArray)
			print str(formulaArray) +  '; mass: ' + str(mass)
			if len(fragmentsToTest) > 2:							# new loop conditional
				highnum = int(mass/fragMass[fragmentsToTest[2]]) + 2
				for k in range(0, highnum):
					formulaArray[2] = [fragmentsToTest[2],k]
					mass = getMass(formulaArray)
					print str(formulaArray) +  '; mass: ' + str(mass)
					if len(fragmentsToTest) > 3:					# new loop conditional
						highnum = int(mass/fragMass[fragmentsToTest[3]]) + 2
						for l in range(0, highnum):
							formulaArray[3] = [fragmentsToTest[3],l]
							mass = getMass(formulaArray)
							print str(formulaArray) +  '; mass: ' + str(mass)
							if len(fragmentsToTest) > 4:					# new loop conditional
								highnum = int(mass/fragMass[fragmentsToTest[4]]) + 2
								for m in range(0, highnum):
									formulaArray[4] = [fragmentsToTest[4],m]
									mass = getMass(formulaArray)
									print str(formulaArray) +  '; mass: ' + str(mass)


'''
def findFragments(formulaArray, counter):
	mass = getMass(formulaArray)
	print counter
	highnum = int(mass/fragMass[fragmentsToTest[counter]]) + 2
	for i in range(0, highnum):
		if formulaArray[-1][0] == fragmentsToTest[counter]:
			formulaArray.pop()
		formulaArray.append([fragmentsToTest[counter],i])
		mass = getMass(formulaArray)
		print str(formulaArray) +  '; mass: ' + str(mass)
		if counter < len(fragmentsToTest) - 1:
			counter += 1
			things = findFragments(formulaArray, counter)
			print things
		else:
			return 'done'

formulaArray = []
counter = 0 #len(fragmentsToTest)

highnum = int(mass/fragMass[fragmentsToTest[counter]]) + 2
for i in range(0, highnum):
	formulaArray.append([fragmentsToTest[counter],i])
	mass = getMass(formulaArray)
	print str(formulaArray) +  '; mass: ' + str(mass)
	if counter < len(fragmentsToTest) - 1:
		counter += 1
		things = findFragments(formulaArray, counter)
		print things
'''




'''

'''




'''
highnum = int(mass/fragMass[fragmentsToTest[0]]) + 2
for i in range(0, highnum):
	formulaArray.append([fragmentsToTest[0],i])
	mass = getMass(formulaArray)
	print str(formulaArray) +  '; mass: ' + str(mass)
	highnum = int(mass/fragMass[fragmentsToTest[1]]) + 2
	for i in range(0, highnum):
		if formulaArray[-1][0] == fragmentsToTest[1]:
			formulaArray.pop()
		formulaArray.append([fragmentsToTest[1],i])
		mass = getMass(formulaArray)
		print str(formulaArray) +  '; mass: ' + str(mass)
'''

'''		
		highnum = int(mass/fragMass[fragmentsToTest[2]]) + 1
		for i in range(0, highnum):
			if formulaArray[-1][0] == fragmentsToTest[2]:
				formulaArray.pop()
			formulaArray.append([fragmentsToTest[2],i])
			mass -= fragMass[fragmentsToTest[2]] * i
			print 'formulaArray: ' + str(formulaArray)
			print 'mass after append: ' + str(mass)
'''





'''
print fragMass['OPiv']
def checkMass(mass, peak, counter, formulaArray, candidateIdentities):
	print 'mass ' + str(mass) + ' start function'
	#print mass
	print 'counter ' + str(counter)
	highnum = int(mass/float(fragMass[fragmentsToTest[counter]])) + 2
	print 'highnum ' + str(highnum)
	thingsAddedThisLoop = 0
	for i in range(0, highnum): 
	#int(fragMass[fragmentsToTest[counter]])):
		#print str(i) + ' ' + fragmentsToTest[counter]
		testMass = mass - fragMass[fragmentsToTest[counter]]
		if testMass >= 0 or abs(testMass) < 0.01:
			#print fragMass[fragmentsToTest[counter]]
			mass = mass - fragMass[fragmentsToTest[counter]]
			thingsAddedThisLoop += 1
			print 'i ' + str(i)	
			formulaArray.append(fragmentsToTest[counter])
			print formulaArray
			print 'mass ' + str(mass) + ' after formulaArray append'
			if abs(mass) < 0.01:
				print "----------------------------------------Candidate:"
				print formulaArray
				print 'endAppend'
				candidateIdentities.append(formulaArray)
				for i in range(thingsAddedThisLoop):
					formulaArray.pop()
					mass += fragMass[fragmentsToTest[counter]]
					print 'popped'
				print formulaArray
				counter -= 2
		else:
			print 'else'
			for i in range(thingsAddedThisLoop):
				formulaArray.pop()
				mass += fragMass[fragmentsToTest[counter]]
				print 'popped'
			print formulaArray
			#delete things added to formulaArray this loop
			counter -= 2
		allSame = False
		print 'mass - fragMass[fragmentsToTest[0]] ' + str(mass - fragMass[fragmentsToTest[0]])
		if mass - fragMass[fragmentsToTest[0]] < -0.01:
			if formulaArray.count(formulaArray[0]) == len(formulaArray):	
				allSame = True		
				#return 'done'
		if counter < len(fragmentsToTest)-1 and allSame != True:
			print 'calling function'
			counter +=1
			checkMass(mass, peak, counter, formulaArray, candidateIdentities)			
mass = peak
formulaArray = []
candidateIdentities = []
counter = 0
status = checkMass(mass, peak, counter, formulaArray, candidateIdentities)
print status
print candidateIdentities
'''

'''
with open('fragments.txt','r') as f:
	doc = f.read()
lines = doc.split('\n')
line = []
for i in lines:
'''	
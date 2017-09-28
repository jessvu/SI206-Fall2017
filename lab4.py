import re
#f = open('mbox-short.txt')
#f = f.readlines()

#numlist = list()
#for line in f:
	#line = line.rstrip()
	#email = re.findall('From',line)
	#if len(email) != 0:
		#print(line)

	#stuff = re.findall('^X-DSPAM-Confidence: ([0-9]+)',line)
	#if len(stuff) != 1: continue
	#num = float(stuff[0])
	#numlist.append(num)

#print(numlist)
#print('Number of Values:',len(numlist))
#print('Maximum:', max(numlist))
#print('Minimum:', min(numlist))
#print('Average:', "{:.3f}".format(sum(numlist)/len(numlist)))

with open("mbox-short.txt", "r") as f:
	f = f.readlines()
	for line in f:
		if re.search('From',line):
			print(line)
			numbers = re.findall('[0-9]+',line)
			print(numbers)
			name = re.findall('(\S*)@',line)
			print(name)
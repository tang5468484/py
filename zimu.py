import time
import os
def chuli(ca):
	c1 = 0
	t2 = [3600, 60]
	t1 = ca.split(':')
	
	for i in range(2):
		c1 =float( t1[i] ) * t2[i]
	c1 += float( t1[2] )
	return c1
	

a = 0
ab = []

with open(input("Please enter ass subtitles lacation>")) as f:
	while("Dialogue: " not in f.readline()):
		a = f.tell()
		
	for i in range(1208):	
		#Dialogue: 
		f.seek(a + 12)
		#0,0:00:00.00start
		e0 = f.read(10)
		g0 = chuli(e0)
		#,
		f.seek(f.tell() + 1)
		#0,0:00:00.00end
		e1 = f.read(10)
		g1 = chuli(e1)
		#BLC,NTP0000000,abfjdsf
		f.seek(f.tell() + 25)
		f1 =f.readline()
		
		#add
		ab.append([g0, g1, f1[:-1] ])
		a = f.tell()

#---------------------------------------------------------------------
offst = input("-->")
offst = float(offst)
i1 = 0
dq = -1
#have a space
dpq = False
time2 = time.time() - offst
length1 = len(ab)
qw = 0.0
er = 0.0


print('\n' * 5)
while i1 < length1:
	time1 = time.time() - time2
	
	if ( time1 >= ab[i1][0] and time1 <= ab[i1][1] ):
		if i1 == dq:
			pass
		else:
			print("\n\n\n{0:^40}".format(ab[i1][2]))
			dq = i1
			dpq = False
			
			
	elif time1 < ab[i1][0]:
		pass
	else:
		if not dpq:
			print('\n' * 5)
			dpq = True	
		i1 += 1

	time.sleep(0.1)
		
		
		
	
	

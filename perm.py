import itertools

a = [0,2,3,4,5,6,7,8,9]
k = 8

for p in itertools.permutations(a,k):
	x = p[0]*10 + p[1] - p[2]*10 - p[3]
	y = p[4]*10 + p[5]
	z = p[6]*10 + p[7]
	
	if (x == y and y+z == 111 and (p[0] != 0) and (p[2]!=0) and (p[4]!=0)and (p[6]!=0)):
		print p



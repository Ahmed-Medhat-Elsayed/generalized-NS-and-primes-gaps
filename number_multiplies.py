import math

# find all multiples of a factor in between region [factor:numbers sample]
def multiplies(end,factor):
	l=[]
	for i in range(factor,math.floor(end/factor)+1):
		l.append(i*factor)
	return l

#removes factors of a number from a number list
def RemoveFators(l,end,factor):
	for i in multiplies(end,factor):
		try:
			l.remove(i)
		except Exception :
			pass

n=10000

l=list(i for i in range(2,n+1))
lo=list(i for i in range(2,n+1))

p1=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]#  97, 101]
p2=[2, 3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101]#,   101]

for i in p1:
	RemoveFators(l,n,i)


for i in p2:
	RemoveFators(lo,n,i)


m=[]

for i in l:
	if i not in lo:
		m.append(i)


for i in m:
	print(i)

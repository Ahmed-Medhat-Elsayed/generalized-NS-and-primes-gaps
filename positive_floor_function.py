import math

def f(j,i,m):
	f= ((i-(j+1))/m)+1
	if f <= 0:
		f=0
	else:
		f=math.floor(f)
	return f




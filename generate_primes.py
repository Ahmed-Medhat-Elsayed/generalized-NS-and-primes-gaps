import math

def Find_Multiplies(_range,factor):
	res=[]
	for i in range(factor,math.floor(_range/factor)+1):
		res.append(i*factor)
	return res

def GeneratePrimes(_range,primes):
	res=list(range(2,_range+1))
	for p in primes:
		for i in Find_Multiplies(_range,p):
			try:
				res.remove(i)
			except Exception:
				pass
	return res










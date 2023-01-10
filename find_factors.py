p=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109]


def defination(_input,prime):
	ref=[]
	for i in p[0:p.index(prime)]:
		if _input/i == int(_input/i):
			ref.append(i)
		else:
			pass
	return ref

def find_factors(prime,_range):
	res=[]
	for i in range(2,_range+1):
		if i/prime == int(i/prime) and len(defination(i,prime))==0:
			res.append(i)
		else:
			pass
	return res

def find_rough_numbers(prime,_range):
	res=[]
	for i in find_factors(prime,_range):
		res.append(int(i/prime))
	return res

def find_difference(_list):
	res=[]
	for i in range(len(_list)-1):
		res.append(int(_list[i+1]-_list[i]))
	return res


def run():
	for pr in p:
		range_=100000000
		c=find_factors(pr,range_)
		l=find_difference(c)
		n=len(l)
		c2=find_rough_numbers(pr,range_)
		with open(f'{pr}.wpd','w') as f:
			f.write('Name:')
			f.write('\nNumbers whose smallest prime factor is '+str(pr))
			f.write('\n\nOffset:')
			f.write('\n1,1')
			f.write('\n\nData (First 30 terms): ')
			f.write('\n'+ str(c[0:30]))
			f.write('\n\nSet of CAFs found: ')
			for i in set(l):
				f.write('\n')
				f.write(f'{i}: {(l.count(i)/n)*100}%')
			f.write('\n\nData: (Up to '+str(len(c))+")")
			f.write('\n')
			f.write('n'+"       |"+'a(n)'+"    |"+f'a(n)/{pr}'+"   |"+f'a(n+1)-a(n)'+"  |"+f'[a(n+1)-a(n)]/{pr}')
			for (i,j,k,x,y) in zip(c,range(1,len(c)+1),c2,l,find_difference(c2)):
				f.write('\n')
				f.write(str(j)+" "*(8-len(str(j)))+"|"+str(i)+" "*(8-len(str(i)))+"|"+str(k)+" "*(9-len(str(k)))+"|"+str(x)+" "*(13-len(str(x)))+"|"+str(y))



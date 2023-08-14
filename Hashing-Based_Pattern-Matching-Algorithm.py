import random
import math
#To check if a number is prime
def isPrime(q):
	if(q > 1):
		for i in range(2, int(math.sqrt(q)) + 1):
			if (q % i == 0):
				return False
		return True
	else:
		return False

#To generate random prime less than N
def randPrime(N):
	primes = []
	for q in range(2,N+1):
		if(isPrime(q)):
			primes.append(q)
	return primes[random.randint(0,len(primes)-1)]

#pattern matching
def randPatternMatch(eps,p,x):
	N = findN(eps,len(p))
	q = randPrime(N)
	return modPatternMatch(q,p,x)

#pattern matching with wildcard
def randPatternMatchWildcard(eps,p,x):
	N = findN(eps,len(p))
	q = randPrime(N)
	return modPatternMatchWildcard(q,p,x)

#return appropriate N that satisfies the error bounds
def findN(eps,m):
	return int(4*(m/eps)*(math.log2(26))*(math.log2((m/eps)*(math.log2(26)))))

#Return sorted list of starting indices where p matches x
def modPatternMatch(q,p,x):
	L=[]
	i=0
	pattern_value=0
	text_value=0
	if len(p)==0:
		return L 
	while i<len(p):
		pattern_value+=(26**(len(p)-i-1))*(ord(p[i])-ord("A"))
		text_value+=(26**(len(p)-i-1))*(ord(x[i])-ord("A"))
		i+=1
	pattern_value=pattern_value%q
	j=0
	while(j<(len(x)-len(p)+1)):
		if pattern_value==text_value%q:
			L.append(j)
			if j<(len(x)-len(p)):
				text_value=(text_value-(26**(len(p)-1))*(ord(x[j])-ord("A")))*26+(ord(x[len(p)+j])-ord("A"))
				j+=1
			else:
				j+=1
		else:
			if j<(len(x)-len(p)):
				text_value=(text_value-(26**(len(p)-1))*(ord(x[j])-ord("A")))*26+(ord(x[len(p)+j])-ord("A"))
				j+=1
			else:
				j+=1
	return L			
#Return sorted list of starting indices where p matches x
def modPatternMatchWildcard(q,p,x):
	L=[]
	i=0
	pattern_value=0
	text_value=0
	if len(p)==0:
		return L 
	while i<(len(p)):
		if p[i]=="?":
		    index_1=i
		    text_value+=(26**(len(p)-i-1))*(ord(x[i])-ord("A"))
		    pattern_value+=(26**(len(p)-i-1))*(ord(x[i])-ord("A"))
		    i+=1
		else:
			pattern_value+=(26**(len(p)-i-1))*(ord(p[i])-ord("A"))
			text_value+=(26**(len(p)-i-1))*(ord(x[i])-ord("A"))
			i+=1
	j=0
	index_2=index_1
	while j<(len(x)-len(p)+1):
		if (pattern_value%q)==(text_value%q):
			L.append(j)
			if j<(len(x)-len(p)):
				text_value=(text_value-(26**(len(p)-1))*(ord(x[j])-ord("A")))*26+(ord(x[len(p)+j])-ord("A"))
				pattern_value=(pattern_value-(26**(len(p)-index_1-1))*(ord(x[index_2])-ord("A")))+(26**(len(p)-index_1-1))*(ord(x[index_1+j+1])-ord("A"))
				index_2=index_1+j+1
				j+=1
			else:
				j+=1
		else:
			if j<(len(x)-len(p)):
				text_value=(text_value-(26**(len(p)-1))*(ord(x[j])-ord("A")))*26+(ord(x[len(p)+j])-ord("A"))
				pattern_value=(pattern_value-(26**(len(p)-index_1-1))*(ord(x[index_2])-ord("A")))+(26**(len(p)-index_1-1))*(ord(x[index_1+j+1])-ord("A"))
				index_2=index_1+j+1
				j+=1
			else:
				j+=1
	return L			
		
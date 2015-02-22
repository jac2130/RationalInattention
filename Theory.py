from random import random, choice

def random_count_sequence(K, T):
    positions=[0]*K
    for i in range(T):
        index=choice(range(K))
	positions[index]+=1
 	return positions

def freqs(ls):
    norm = sum(ls)
    return [num/float(norm) for num in ls]

def optprior(K, T, old=[]):
    old=random_count_sequence(K, T-1) if old==[] else old
    new=[o+1/float(K) for o in old]
    return [num/float(T) for num in new]

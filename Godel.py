from fractions import Fraction

def G(k):
    return [0, *[Fraction(i+1,k-1) for i in range(k-2)], 1]

def min(u,v):
    if u > v: return v
    elif v > u: return u
    else: return u

def max(u,v):
    if u > v: return u
    elif v > u: return v
    else: return u

def neg(u):
    if u == 0: return 1
    elif u > 0: return 0

def implication(u,v):
    if u <= v: return 1
    elif u > v: return v

def imin(u,v):
    if(u and v <= 1 and u and v >= 0):
        min(u,v)

def imax(u,v):
    if(u and v <= 1 and u and v >= 0):
        max(u,v)

def ineg(u):
    if(u <= 1 and u >= 0):
        neg(u)   

def iimplication(u,v):
    if(u and v <= 1 and u and v >= 0):
        implication(u,v)

AND = min
OR = max
NOT = neg
IMP = implication

IAND = imin
IOR = imax
INOT = ineg
IIMP = iimplication
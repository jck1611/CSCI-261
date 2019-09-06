y = []

def r(list):
    if (list == []):
        return []
    else:
        y.append(list[0])
        list.pop(0)
        r(list)
    return y

def prod(m,n):
    if (m == 0):
        return 0
    else:
        return prod(m-1,n) + n

def fastPow(b,k):
    if (k == 0):
        return 1
    if (k%2 == 0):
        return (b**2)**(k//2)
    if (k%2 == 1):
        return ((b**2)**(k//2))*b

def prodAccum(m,n,a):
    if (m == 0):
        return a
    else:
        return prodAccum(m-1,n,n+a)

def min(a,b):
    if (a == None and b != None):
        return b
    if (a != None and b == None):
        return a
    if(a == None and b == None):
        return None
    if (a < b):
        return a
    if (b < a):
        return b

def failAdd(a,b):
    if (a == None or b == None):
        return None
    else:
        return a + b

def minChange(a,dList):
    if (a == 0):
        return 0
    if (dList == []):
        return None
    if (dList[0] > a):
        dList.pop(0)
        return minChange(a,dList)
    else:
        return min(failAdd(1,minChange(a-dList.pop(0),dList)),minChange(a,dList))

def quotient(a,d):
    return a//d

def remainder(a,d):
    return a%d

def greedyMinChange(a,dList):
    if (a == 0):
        return 0
    if (dList == []):
        return None
    if (dList[0] > a):
        dList.pop(0)
        return greedyMinChange(a,dList)
    else:
        return failAdd(quotient(a,dList[0]), greedyMinChange(remainder(a,dList[0]), dList))

def powIt(a,b):
    n = 1
    while (b > 0):
        n = n*a
        b-=1
    return n

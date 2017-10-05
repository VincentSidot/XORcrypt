hex = [chr(ord('0')+i) for i in range(0,10)] + [chr(ord('a')+ i) for i in range(0,6)]
def B2D(n,B=2):
    rep = 0
    for i in n:
        rep = rep*B + i
    return rep

def D2B(n,B=2):
    L = []
    while n > 0:
        r,n = n%B,n//B
        L = [r] + L
    return L
    
def HashlibToInt(_hashlib):
    str = _hashlib.hexdigest()
    L = []
    for i in str.lower():
        try:
            L += [hex.index(i)]
        except:
            L = L
    return B2D(L,16)

def nextCongruential(Xn): #générateur de Haynes
    return (Xn * 6364136223846793005)%2**64

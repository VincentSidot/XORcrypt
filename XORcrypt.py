import utils
alphabet = [chr(ord('A') + i) for i in range(0,26)] + [chr(ord('a') + i) for i in range(0,26)] + [chr(ord('0') + i) for i in range(0,10)]


def XORcrypt(str,key):
    rep = []
    for i in range(0,len(str)):
        try:
            rep += chr(ord(alphabet[(alphabet.index(str[i])^alphabet.index(key[i%len(key)]))%len(alphabet)]))
        except:
            rep += [' ']
    return ''.join(rep)

def XORdecrypt(str,key):
    return XORcrypt(str,key)
    
def CesarCrypt(str,key):
    rep = []
    for i in range(0,len(str)):
        try:
            rep += chr(ord(alphabet[(alphabet.index(str[i])+alphabet.index(key[i%len(key)]))%len(alphabet)]))
        except:
            rep += [' ']
    return ''.join(rep)

def CesarDecrypt(str,key):
    rep = []
    for i in range(0,len(str)):
        try:
            rep += chr(ord(alphabet[(alphabet.index(str[i])-alphabet.index(key[i%len(key)]))%len(alphabet)]))
        except:
            rep += [' ']
    return ''.join(rep)

    
def PMSCrypt(str,key):
    rep = []
    j=1
    for i in range(0,len(str)):
        try:
            rep += chr(ord(alphabet[(alphabet.index(str[i])+j*alphabet.index(key[i%len(key)]))%len(alphabet)]))
            j+=1
        except:
            if str[i] != ' ' and str[i] != '\n':
                j+=1
            rep += str[i]
    return ''.join(rep)

def PMSDecrypt(str,key):
    rep = []
    j=1
    for i in range(0,len(str)):
        try:
            rep += chr(ord(alphabet[(alphabet.index(str[i])-j*alphabet.index(key[i%len(key)]))%len(alphabet)]))
            j+=1
        except:
            if str[i] != ' ' and str[i] != '\n':
                j+=1
            rep += str[i]
    return ''.join(rep)


def CongruentialCrytp(str,key):
    import hashlib
    Xn = utils.HashlibToInt(hashlib.sha256(key.encode()))
    L = []
    for i in str:
        try:
            L += chr(ord(alphabet[(alphabet.index(i) + Xn)%len(alphabet)]))
            Xn = utils.nextCongruential(Xn)
        except:
            L += [' ']
    return ''.join(L)

def CongruentialDerypt(str,key):
    import hashlib
    Xn = utils.HashlibToInt(hashlib.sha256(key.encode()))
    L = []
    for i in str:
        try:
            L += chr(ord(alphabet[(alphabet.index(i) - Xn)%len(alphabet)]))
            Xn = utils.nextCongruential(Xn)
        except:
            L += [' ']
    return ''.join(L)
    
def CongruentialPMSCrytp(str,key):
    import hashlib
    Xn = utils.HashlibToInt(hashlib.sha256(key.encode()))
    L = []
    for i in range(0,len(str)):
        try:
            L += chr(ord(alphabet[(alphabet.index(str[i]) + i*Xn)%len(alphabet)]))
            Xn = utils.nextCongruential(Xn)
        except:
            L += [' ']
    return ''.join(L)

def CongruentialPMSDerypt(str,key):
    import hashlib
    Xn = utils.HashlibToInt(hashlib.sha256(key.encode()))
    L = []
    for i in range(0,len(str)):
        try:
            L += chr(ord(alphabet[(alphabet.index(str[i]) - i*Xn)%len(alphabet)]))
            Xn = utils.nextCongruential(Xn)
        except:
            L += [' ']
    return ''.join(L)
    
    

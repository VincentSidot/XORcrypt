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

import math

def syndrome(v, n, k):
    p = math.ceil(math.log2(k))
    h = [0]*4
    for i in range(0, p):
        h[i] = sum([int(v[n-1-j]) if (bin(j + 1)[2:].zfill(p)[i] == '1') else 0 for j in range(0, n)]) % 2
    c = 0
    for i in range(0, len(h)):
        c = c*2 + h[i]
    return c

def decode(v, c, n, k):
    c = len(v) - c
    if c != 15:
        vne = v[:c] + str(int(not int(v[c]))) + v[c+1:]
    else:
        vne = v

    return vne


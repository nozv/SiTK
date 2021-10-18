import math


def encode(v, n, k):
    x = iter(reversed(v))
    p = math.ceil(math.log2(k))
    a = [0 if (i==1) or (math.log2(i) % 1==0) else int(next(x)) for i in range(1, n+1)]
    for i in range(0, p):
        a[pow(2,i)-1] = sum([int(a[j]) if (bin(j+1)[2:].zfill(p)[i] == '1') and (j+1 != pow(2,i)-1) else 0 for j in range(0, n)])%2
    s = ''.join(str(i) for i in list(reversed(a)))
    return s



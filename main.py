import math
from hamming.encode import encode
from hamming.decode import decode
from hamming.decode import syndrome
from output import output


def main():

    v = '01010101111'               # заданный вариантом информационный вектор
    n = 15
    k = 11
    cin = [0.0]*n                   # общее число ошибок i-й кратности
    nk = [0]*n                      # число исправленных ошибок i-й кратности
    det = [0]*n                     # число обнаруженных ошибок i-й кратности
    ck = [0.0]*n                    # корректирующая способность

    vd = encode(v, n, k)
    for i in range(1, pow(2, n)):
        e = bin(i)[2:].zfill(n)     # вектор ошибки
        kr = e.count('1')           # кратность ошибки
        ve = ''.join(str(j) for j in [int(vd[q]) ^ int(e[q]) for q in range(0, n)])

        s = syndrome(ve, n, k)
        if s != 0:
            det[kr-1] += 1          # если синдром != 0, то обнаружена ошибка
        if vd == decode(ve, s, n, k):
            nk[kr-1] += 1           # если декодированная строка != закодированной, то ошибка не исправлена

    for i in range(0, n):
        cin[i] = math.factorial(n)/(math.factorial(i+1)*math.factorial(n-i-1))
        ck[i] = nk[i]/cin[i]*100

    #print('\033[1mРезультаты\033[0m')
    output(n, ck, nk, det, cin)


if __name__ == '__main__':
    main()


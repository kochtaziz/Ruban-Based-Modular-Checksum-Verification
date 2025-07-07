from numpy import *

def puis(x, y):
    p = 1
    for i in range(y):
        p *= x
    return p

def Ruban(k, d):
    ch = str(k)
    l = len(ch) - 1
    t = ""
    for i in range(len(ch)):
        t += str(puis(10, l) % d)
        l -= 1
    return t

def somme(t, k):
    s = 0
    ch = str(k)
    for i in range(len(ch)):
        s += int(t[i]) * int(ch[i])
    return s

def verif(k, d):
    while True:
        t = Ruban(k, d)
        s = somme(t, k)
        if s == d:
            return True, k, t, s
        if s == k:  # Stuck in a

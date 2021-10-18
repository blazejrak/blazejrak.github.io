from math import sqrt
from random import randrange
def sort(tab, i = 0):
    i, tab = 0, []
    while i < len(tab) - 1:
        j = 0
        while j < len(tab) - 1:
            if tab[j] > tab[j + 1]:  
                tab[j], tab[j + 1] = tab[j + 1], tab[j]
            j+= 1
        i+=1
    return tab
def x(x):
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True
def ax(l, a = []):
    for i in range(2, l):
        if x(i):
            a.append(i)
    return a
def s(y, z):
    def sp(y, z):
        print("źle podałeś " + y + ". powtórz")
        return s(y, z)
    try:
        x = input("podaj " + y + " ")
        if z == 1:
            if int(x) >= 43:
                return int(x)
            else:
                return sp(y, z)
        elif z == 0:
            if "tak" == x or "nie" == x:
                return x
            else:
                return sp(y, z)
        else:
            return str(x)
    except ValueError:
        return sp(y, z)
m, pp, mp = s("iformacje do zaszyfrowania", 2), [], s("chcesz widzieć potęgi(tak/nie)", 0)
a = s("komplikacje szyfrowania", 1)
ppq = ax(a)
print(ppq)
p = ppq[randrange(10, len(ppq))]
q = p
while p == q:
    q = ppq[randrange(13, len(ppq))]
n, c = p * q, []
po = ax(n - randrange(1, n - 1))
e, d = po[len(po) - 1], 0
fi, pf, t, u = (p-1) * (q-1), [], [], []
while (d * e) % fi != 1:
    d += 1
for i in m:
    c.append((ord(i) ** e) % n)
    u.append(ord(i) ** e)
    print("wartość z ASCII: {a} (znak:{b})".format(a = ord(i), b = i))
    pf.append(ord(i) <=  n)
for i in c:
    t.append(chr(i))
if mp == "tak":
    print("m do potęgi e: {pa}".format(pa = u))
print("wylosowana liczba pierwsza p: {e}\nwylosowana liczba pierwsza q:{f} \np*q: {c} \nwylosowana mniejsza od (p*q): {d} \nklucz: {b} \nszyfr: {a}\nszyfr na ASCII: {aA}".format(a = c, b = d, c = n, d = e, e = p, f = q, aA = "".join(t)))
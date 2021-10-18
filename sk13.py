def p(x, y = [], z = []):
    for i in x:
        if i == ",":
            z.append(y)
            y = []
        else:
            y.append(i)
    z.append(y)
    y = []
    for i in z:
        y.append(int("".join(i)))
    return y
def s(y, z):
    def sp(y, z):
        print("źle podałeś " + y + ". powtórz")
        return s(y, z)
    try:
        x = input("podaj " + y + " ")
        if z == 1:
            return int(x)
        elif z == 0:
            if type(int(x.replace(", ", ""))) != str:
                return list(x.replace(" ", ""))
        elif z == 2:
            if "tak" == x or "nie" == x:
                return x
            else:
                return sp(y, z)
    except ValueError or TypeError:
        return sp(y, z)
c, d, n, w, x, y, z = p(s("szyfr", 0)), s("klucz", 1), s("p*q", 1),s("czy chcesz widzieć potęgi(nie/tak)", 2), [], [], []
for i in c:
    x.append((i ** d) % n)
    z.append(i ** d)
    y.append(chr((i ** d) % n))
if w == "tak":
    print("c do potęgi d: {a}".format(a = z))
print("wynik ASCII: {a} \nwyniki str(surowe): {b}\nwyniki str(obrobione): {c}".format(a = x, b = y, c = "".join(y)))
#2412, 1120, 2412, 2060, 144, 2412, 2060, 471, 3041, 1366, 2412
#2897
#3139
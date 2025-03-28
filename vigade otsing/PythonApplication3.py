import math

# Ruudu karakteristikud
print("Ruudu karakteristikud")
try:
    a=float(input('Sisesta ruudu külje pikkus=>'))
    S=a**2
    print("Ruudu pindala:",S)
    P=4*a
    print("Ruudu ümbermõõt:",P)
    di=a*math.sqrt(2)
    print("Ruudu diagonaal:",round(di,2))
except ValueError:
    print("Palun sisesta kehtiv arv ruudu külje pikkuseks.")

print()

# Ristküliku karakteristikud
print("Ristküliku karakteristikud")
try:
    b=float(input("Sisesta ristküliku 1. külje pikkus=>"))
    c=float(input("Sisesta ristküliku 2. külje pikkus=>"))
    S=b*c
    print("Ristküliku pindala:",S)
    P=2*(b+c)
    print("Ristküliku ümbermõõt:",P)
    di=math.sqrt(b**2+c**2)
    print("Ristküliku diagonaal:",round(di,2))
except ValueError:
    print("Palun sisesta kehtivad arvud ristküliku külgede pikkuseks.")

print()

# Ringi karakteristikud
print("Ringi karakteristikud")
try:
    r=float(input("Sisesta ringi raadiusi pikkus=>"))
    d=2*r
    print("Ringi läbimõõt:",d)
    S=math.pi*r**2
    print("Ringi pindala:",round(S,2))
    C=2*math.pi*r
    print("Ringjoone pikkus:",round(C,2))
except ValueError:
    print("Palun sisesta kehtiv arv ringi raadiuse pikkuseks.")

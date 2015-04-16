print("Ejercicio 3")
def superpower(n,e):
    if e==0:
        return 1
    r = n
    for a in range (e-1):
        r*=n
    return r
n=int(input("Dame el numero que quieres elevar "))
e=int(input("Dame la potencia a la que quieres elevar "))
print(superpower(n,e))

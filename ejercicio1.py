print("Ejercicio 1")
def raiz(n):
    x= n/2
    y= x+1
    while(x!=y):
        z= n/x
        y= x
        x= (x+z)/2
    return x
def hipo(x1,y1,x2,y2):
    a=(x2-x1)
    b=(y2-y1)
    x=(a*a)+(b*b)
    y= raiz(x)
    return y

x1=int(input("Dame la posicion x1 del triangulo "))
x2=int(input("Dame la posicion x2 del triangulo "))
y1=int(input("Dame la posicion y1 del triangulo "))
y2=int(input("Dame la posicion y2 del triangulo "))

print(hipo(x1,x2,y1,y2))

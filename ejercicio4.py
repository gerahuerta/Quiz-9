print("Ejercicio 4")
def fibonacci(n):
    a,b=0,1
    for i in range(n):
        a,b=b,a+b
    return a
n=int(input("Dame el numero que quieres usarl la funcion"))
print(fibonacci(n))       

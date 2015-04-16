def triangulo(size):
    for i in range(1,size+1):
        for j in range(i):
            print("T", end="")
        print()
    for i in range(1,size+1):
        for j in range(size-i+1):
            print("T", end="")
        print()
size=int(input("Dame la anchura del triangulo"))
h=triangulo(size)

# Actividad 2
print('----------------------------------------------------------------')
import math

# Ejercicio 1
def rectangulo(b,h):
    a=b*h
    print (f'El área del rectángulo es {a}')

rectangulo(15,10)

print('----------------------------------------------------------------')

# Ejercicio 2

def circulo(r):
    a = (math.pi)*r**2
    print (f'El área del cirulo radio {r} es igual a {a}')

circulo(5)

print('----------------------------------------------------------------')

# Ejercicio 3

def relacion(n1,n2):
    if n1>n2:
        r=1
    elif n1<n2:
        r=-1
    elif n1==n2:
        r=0
    return r

print(relacion(5,10))
print(relacion(10,5))
print(relacion(5,5))


print('----------------------------------------------------------------')

# Ejercicio 4

def intermedio(n1,n2):
    i=(n1+n2)/2
    return i

print (intermedio(-12,24))


print('----------------------------------------------------------------')

# Ejercicio 5

def recortar(a,b,c):
    if a<b:
        return b
    elif a>c:
        return c
    elif a<b and a<c:
        return a
    

print(recortar(15,0,10))

print('----------------------------------------------------------------')


def separar(lista):
    par=[]
    impar=[]
    for i in lista:
        if i%2==0:
            par.append(i)
        else:
            impar.append(i)
    return f'Lista pares {par} --- lista impares {impar}'

num=[2,3,5,7,8,9,12,14,17]

print(separar(num))


'''
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
'''

#Librerias que necesitamos

import math

# Comprobación primo

def primo(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# Comprobación Fibonacci

def fibonacci(num):
    a=0
    b=1
    # Usamos un bucle con while para iterar desde a y b (0,1)
    while b < num:
        a, b = b, a + b
    return b == num

#Comprobación par

def par(num):
    return num % 2 == 0


# Definimo num mediante input al usuario

num = int(input("Introduce un número: "))

if primo(num):
    print("Es primo.")
else:
    print("No es primo.")

if fibonacci(num):
    print("Es fibonacci.")
else:
    print("No es fibonacci.")

if par(num):
    print("Es par.")
else:
    print("No es par.")
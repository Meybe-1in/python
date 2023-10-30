#1) Programa una función que cuente el número de caracteres de una cadena de texto, pe. miFuncion("Hola Mundo") devolverá 10.


def contador_de_caracteres(str):
    '''print(len(str))'''
contador_de_caracteres("hola e")

#2) Programa una función que te devuelva el texto recortado según el número de caracteres indicados,
# pe. miFuncion("Hola Mundo", 4) devolverá "Hola".

def slice_string (str, length):
    x = slice(length)
   # print (str[x])
slice_string("hola Dayana", 8)


#3) Programa una función que dada una String te devuelva un Array de textos separados por cierto caracter, 
# pe. miFuncion('hola que tal', ' ') devolverá ['hola', 'que', 'tal'].

def slice_string (str, separator):
    x = str.split(separator)
    #print (x)
slice_string("hola Dayana como estas", " ")


#4) Programa una función que repita un texto X veces, pe. miFuncion('Hola Mundo', 3) devolverá Hola Mundo Hola Mundo Hola Mundo.

def repeat_text(str, repeatt):
    str_repeat = str * repeatt
    #print (str_repeat)
repeat_text ("hola ", 3)

def repeat_text1(str, repeatt):
    for i in range(repeatt):
       ''' print (str)'''
repeat_text1 ("hola ", 5)
#5) Programa una función que invierta las palabras de una cadena de texto, 
# pe. miFuncion("Hola Mundo") devolverá "odnuM aloH".

def invert_string(str):
    inverted_string = ""
    for i in str:
        inverted_string = i + inverted_string
    #print (inverted_string)
invert_string("hola como estas")

def invertir_cadena(cadena):
    x = cadena[::-1]
    #print(x)
invertir_cadena("no hay clases")


#6) Programa una función para contar el número de veces que se repite una palabra en un texto largo,
#  pe. miFuncion("hola mundo adios mundo", "mundo") devolverá 2.

def count_word(str , word):
    list = str.split(" ")
    repeat = list.count(word)

    #print (repeat)
count_word("hola hola mey", "hola")     

#7) Programa una función que valide si una palabra o frase dada, es un palíndromo (que se lee igual en un sentido que en otro), 
# pe. mifuncion("Salas") devolverá true.

def polindromo(str):
    inverted_string = ""
    for i in str:
        inverted_string = i + inverted_string
    if str == inverted_string:
        '''print("Palindrome")'''
    else:
       ''' print("Not Palindrome")'''
polindromo("salas")

#------------------------------------------------

'''word = input()
if str(word) == "".join(reversed(word)):
    print("Palindrome")
else:
    print("Not Palindrome")
#------------------------------------------------

word = input()
if str(word) == str(word)[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")'''

#8) Programa una función que elimine cierto patrón de caracteres de un texto dado,
#  pe. miFuncion("xyz1, xyz2, xyz3, xyz4 y xyz5", "xyz") devolverá  "1, 2, 3, 4 y 5.

def patron (str, patron):
    new_str = str.replace(patron,'')

    #print(new_str)

patron("xyz1, xyz2, xyz3, xyz4 y xyz5", "xyz")

#9) Programa una función que obtenga un numero aleatorio entre 501 y 600.
import random
def random_num(r1 = 501 , r2 = 600):

    '''print (random.randint(r1, r2))'''
random_num()

#10) Programa una función que reciba un número y evalúe si es capicúa o no 
# (que se lee igual en un sentido que en otro), pe. miFuncion(2002) devolverá true.

def capicua(number):
    
    string = str(number)

    string1 = ""

    for i in string :
        string1 = i + string1
    if string == string1:
        '''print(f'{string} es Capicua')'''
    else:
        '''print(f'{string} no es Capicua')'''

capicua(2003)


#11) Programa una función que calcule el factorial de un número 
# (El factorial de un entero positivo n, 
# se define como el producto de todos los números enteros positivos desde 1 hasta n),
# pe. miFuncion(5) devolverá 120.

def factorial(num):
    if num < 0:
        print (1)

    fac = 1
    i = 1
    while (i <= num):
        fac = fac * i
        i = i + 1
    '''print(fac)'''

factorial(1)

#-------------------------------------------
def factorial(numero):
    if numero < 0:
        print (1)
    factorial = 1
    while numero > 0:
        factorial = factorial * numero
        numero -= 1
    '''print( factorial)'''
factorial (1)

#12) Programa una función que determine si un número es primo (aquel que solo es divisible por sí mismo y 1) o no, 
# pe. miFuncion(7) devolverá true.

def prime_number (num):
    
    for i in range(2, num):
        if num % i == 0:
            print(f'The number {num} is not a prime number')
            return False
    print(f'The number {num} is prime number')
    return True
prime_number(7)


import math

def es_primo(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if (n%i) == 0:
            #print(f'The number {n} is not a prime number')
            return False
    #print(f'The number {n} is prime number')
    return True

es_primo(7)
#13) Programa una función que determine si un número es par o impar, 
# pe. miFuncion(29) devolverá Impar.

def odd_even (num):

    if num % 2 == 0:
        #print(f'The number {num} is even')
        return True
    #print(f'The number {num} is odd')
    return False
odd_even(13)


#14) Programa una función para convertir grados Celsius a Fahrenheit y viceversa, 
# pe. miFuncion(0,"C") devolverá 32°F.

def fahrenheit_celsius():
    
    fahrenheit = int(input('Ingrese la temperatura en grados Fahrenheit: '))
    celsius = (fahrenheit -32 ) * 5.0/9.0
    return '{} grados Fahrenheit son {} grados Celsius'.format(fahrenheit, celsius)
def celsius_fahrenheit():

    celsius = int(input('Ingrese la temperatura en grados Celsius: '))
    fahrenheit = 9.0/5.0 * celsius +32
    return '{} grados Celsius son {} grados Fahrenheit'.format(fahrenheit, celsius)
while True:
    print('1.- Fahrenheit a Celsius')
    print('2.- Celsius a Fahrenheit')
    print('3.- Salir')
    try:
        opcion = int(input('Seleccione una opción: '))
        if opcion == 1:
            print(fahrenheit_celsius())
        elif opcion == 2:
            print(celsius_fahrenheit())
        elif opcion == 3:
            print('Hasta luego')
        else:
            raise ValueError
    except ValueError:
        print('Ingrese solo números.(1/2)')


#15) Programa una función para convertir números de base binaria a decimal y viceversa, 
# pe. miFuncion(100,2) devolverá 4 base 10.


#16) Programa una función que devuelva el monto final después de aplicar un descuento a una cantidad dada, 
# pe. miFuncion(1000, 20) devolverá 800.


#17) Programa una función que dada una fecha válida determine cuantos años han pasado hasta el día de hoy, 
# pe. miFuncion(new Date(1984,4,23)) devolverá 35 años (en 2020).


#18) Comprobar si una cadena Python dada es un palíndromo.


#19) Comprobar si dos cadenas son o no anagramas.


#20) Dada una cadena que contiene el nombre y los apellidos, 
#compruebe si la cadena del nombre está formateada en mayúsculas y minúsculas.
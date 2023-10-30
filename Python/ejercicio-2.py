#le pedimos al usario que escriba
frase = input("Decime una frase y te calculo cuanto tardarias si tuvieras que decirla: ")

#creamos una lista con todas las palabras de la frase( se separan cada vez que hay un espacio en blanco) con split
palabras_separadas = frase.split(" ")

#len para ver la cantidad de elementos que hay en una lista
cantidad_de_palabras = len(palabras_separadas)

#en caso de tardar mas de un minuto
if cantidad_de_palabras > 120:
    print("para tampoco te pedi un testamento")

#calculamos cuanto se tardaria en decirlas palabras y se lo mostramos
print(f'Dijistes {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras/2} segundos en decirlo')
print(f'Dayana lo diria en {cantidad_de_palabras/2*1.3} segundos en decirlo')


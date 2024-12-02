import re
from collections import Counter

print("___________________________________MENÚ______________________")
print("Ingrese el proceso de traducción que requiere")
print("1. Traducción de ADN a ARN")
print("2. Traducción de ARN a ADN")
#Dato ingresable para definir el proceso de traducción
a=input()
#El if que indica si el valor de ingreso es igual a 1 me hace la opción 1 del menú
if a=='1':
        # Diccionario de reemplazos
        #Vector de traduccion
        #Vector en donde cada elemento es la relación de los caracteres a comparar
        reemplazos = {
            'A': 'U',
            'T': 'A',
            'G': 'C',
            'C': 'G'
        }

        # Función para reemplazar usando el diccionario
        def replace(match):
            return reemplazos.get(match.group(0), match.group(0))

        with open('Cadena_ADN.fasta', 'r') as file:
            # Leer todo el contenido del archivo
            content = file.read()

            print("CÓDIGO ORIGINAL")
            print(content)

            #La librería re nos trae la función para cambiar los caracteres de un texto traducido
            #Me almancena los cambios de los nucleotidos en la variable "content_mod"
            #La libería "re" tiene muchas funciones, en este caso llamamos "sub" de substitution para cambiar los valores hallados en la función "replace"
            content_mod = re.sub(r'[ATGC]', replace, content)

            print("CÓDIGO TRADUCIDO")
            print(content_mod)

        # Contar la frecuencia de cada carácter
        contador_C = content_mod.count('C')
        contador_G = content_mod.count('G')
        contador_U = content_mod.count('U')
        contador_A = content_mod.count('A')

        # Mostrar los caracteres que se repiten (si su frecuencia es mayor a 1)
        print("Caracteres que se repiten:")
        print("Número de Citocina: C:", contador_C)
        print("Número de Guanina: G:", contador_G)
        print("Número de Uracilo: U:", contador_U)
        print("Número de Adenina: A:", contador_A)

        #Conteo porcentual
        #La variable T me suma el total de nucleotidos que contiene el texto para hacer los porcentajes
        T=contador_C+contador_A+contador_G+contador_U
        print("Distribución porcentual:")
        #La función round redondea a las cifras deseadas, los argumentos son el número evaluado y el número de decimales
        print("Porcentaje de Citocina: C:", round(contador_C/T*100 , 0) , "%")
        print("Porcentaje de Guanina: G:", round(contador_G/T*100,0),  "%")
        print("Porcentaje de Uracilo: U:", round(contador_U/T*100,0), "%")
        print("Porcentaje de Adenina: A:", round(contador_A/T*100,0), "%")

        with open('Secuencia_Traducida.txt', 'w') as file:
          # Escribimos en el archivo
          file.write("Secuencia Original ADN \n")
          lines = content.splitlines()
          file.write("\n".join(lines[1:]))
          file.write("Secuencia Traducida ARN \n")
          lines1 = content_mod.splitlines()
          file.write("\n".join(lines1[1:]))

          resultado = (
              "Caracteres que se repiten: \n"
              f"Número de Uracilo: U: {contador_C} \n"
              f"Número de Adenina: A: {contador_G} \n"
              f"Número de Guanina: G: {contador_U} \n"
              f"Número de Citocina: C: {contador_A} \n"
              "Distribución porcentual: \n"
              f"Porcentaje de Uracilo: U: {round(contador_C / T * 100, 2)} % \n"
              f"Porcentaje de Adenina: A: {round(contador_G / T * 100, 2)} % \n"
              f"Porcentaje de Guanina: G: {round(contador_U / T * 100, 2)} % \n"
              f"Porcentaje de Citocina: C: {round(contador_A / T * 100, 2)} % \n"
          )
          # Escribir todo en una sola línea
          file.write(resultado)


elif a=='2':
        # Diccionario de reemplazos
        #Vector de traduccion
        reemplazos = {
            'U': 'A',
            'A': 'T',
            'C': 'G',
            'G': 'C'
        }

        # Función para reemplazar usando el diccionario
        def replace(match):
            return reemplazos.get(match.group(0), match.group(0))

        with open('Cadena_ARN.txt', 'r') as file:
            # Leer todo el contenido del archivo
            content = file.read()

            # Realizar los reemplazos usando expresiones regulares
            content_mod = re.sub(r'[UACG]', replace, content)


            print("CÓDIGO ORIGINAL")
            print(content)

            print("CÓDIGO TRADUCIDO")
            print(content_mod)

        # Contar la frecuencia de cada carácter
        contador_T = content_mod.count('T')
        contador_A = content_mod.count('A')
        contador_G = content_mod.count('G')
        contador_C = content_mod.count('C')

        # Mostrar los caracteres que se repiten (si su frecuencia es mayor a 1)
        print("Caracteres que se repiten:")
        print("Número de Tiamina: T:", contador_T)
        print("Número de Adenina: A:", contador_A)
        print("Número de Guanina: G:", contador_G)
        print("Número de Citocina: C:", contador_C)

        #Conteo porcentual
        T=contador_T+contador_A+contador_G+contador_C
        print("Distribución porcentual:")
        print("Porcentaje de Tiamina: T:", round(contador_T/T*100,2) , "%")
        print("Porcentaje de Adenina: A:", round(contador_A/T*100,2),  "%")
        print("Porcentaje de Guanina: G:", round(contador_G/T*100,2), "%")
        print("Porcentaje de Citocina: C:", round(contador_C/T*100,2), "%")

        with open('SecuenciaTraducida.txt', 'w') as file:
          # Escribimos en el archivo
          file.write("Secuencia Original ARN \n")
          lines = content.splitlines()
          file.write("\n".join(lines[1:]))
          file.write("Secuencia Traducida ADN\n")
          lines1 = content_mod.splitlines()
          file.write("\n".join(lines1[1:]))
          resultado = (
              "Caracteres que se repiten: \n"
              f"Número de Uracilo: T: {contador_T} \n"
              f"Número de Adenina: A: {contador_A} \n"
              f"Número de Guanina: G: {contador_G} \n"
              f"Número de Citocina: C: {contador_C} \n"
              "Distribución porcentual: \n"
              f"Porcentaje de Uracilo: U: {round(contador_T / T * 100, 2)} % \n"
              f"Porcentaje de Adenina: A: {round(contador_A / T * 100, 2)} % \n"
              f"Porcentaje de Guanina: G: {round(contador_G / T * 100, 2)} % \n"
              f"Porcentaje de Citocina: C: {round(contador_C / T * 100, 2)} % \n"
          )

          # Escribir todo en una sola línea
          file.write(resultado)

################
# Giuliano Daniele - @MaiandraGD
# UNRN Andina - Introducción a la Ingeniería en Computación
################

from time import time

def factorial(num):                                         #esta función calcula el factorial de un número
    resultado = 1                                           #almaceno la suma de los productos
    for i in range(1, num+1):         
        resultado = resultado * i  
    return(resultado)
          

def factorion(arg):                                         #esta funcion determina si un número es factorión
    
    suma = 0                                                #suma de los factoriales de los digitos del numero
    for i in str(arg):
        suma = suma + factorial(int(i))
    if arg == int(suma):                                    #si la suma de los factoriales de sus digitos es igual al número:
        return True                                       
    else:
        return False


def lista_factoriones():                                    #esta funcion obtiene los primeros 1500000 factoriones
    
    inicio = time()                                         #cronometro el tiempo de inicio
    lista = []                                              #almaceno aquí los números obtenidos
    
    for i in range (1,1500000):
        if factorion(i):                                    #si el número es un factorión, lo añade a la lista
            lista.append(i)
   
    total = round(time()-inicio,1)                          #tiempo total que demoró el programa en obtener la lista
    
    return (lista, total)
    
    
if __name__ == "__main__":
    resultados = (lista_factoriones())
    print(f"Primeros 1.500.000 factoriones: {resultados[0]}")
    print(f'Tiempo total: {resultados[1]}"')
    

            
    
        

################
# Giuliano Daniele - @MaiandraGD
# UNRN Andina - Introducción a la Ingeniería en Computación
################


def divisores (numero):                                     
    
    divisores = [x for x in range(1,numero) if numero % x == 0]   
    return divisores

def perfecto (num):
    
    if num < 0:                                             #si el argumento es un negativo, devuelve los primeros 4 perfectos           
        perfectos = []
        for i in range(9000):        
            if perfecto(i):
                perfectos.append(i)
        return perfectos
    
    elif num == 0:                                          #el cero no es perfecto (lo podría haber resuelto de otra forma esto)
        return False
    
    else:
        suma = sum(divisores(num))                          
        if num == suma:                                     #si la suma de sus divisores es igual al número, es perfecto
            return True
        else:
            return False
    

if __name__ == "__main__":
    print (perfecto(10))
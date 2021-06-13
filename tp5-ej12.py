################
# Giuliano Daniele - @MaiandraGD
# UNRN Andina - Introducción a la Ingeniería en Computación
################

# Esta funcion no analiza si los números se repiten o no

def lista_igual():       
    
    
    lista1 = list(input("Ingrese números para la primer lista: "))
    lista2 = list(input("Ingrese números para la segunda lista: "))
    
    
    #reviso si cada elemento de lista 1 está en lista 2
    for i in lista1:        
        if i not in lista2:
            return False

    #reviso si cada elemento de lista 2 está en lista 1
    for i in lista2:
        if i not in lista1:
            return False

    return True
        
        
def prueba():
   print(lista_igual()) 
    
if __name__ == "__main__":
    prueba()
    
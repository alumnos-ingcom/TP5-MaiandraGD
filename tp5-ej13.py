################
# Giuliano Daniele - @MaiandraGD
# UNRN Andina - Introducción a la Ingeniería en Computación
################

def buscar_palabra(palabra, texto):
    
    """
    Función que retorna la posición de una (palabra) en un (texto)
    El índice comienza en 1. Distingue entre mayúsculas.
    """
    
    lista = [x for x in texto if x not in ",.!?¡¿-_:;()'"] #creo una lista que no contiene símbolos
    lista = "".join(lista) #agrupo las palabras separadas por espacios
    
    lista = lista.split() #convierto en una lista de palabras separadas
           
    
    for i,elemento in enumerate(lista): #recorre la lista en busca de coincidencias
        if elemento == palabra:
            return i+1 #si encuentra la palabra, retorna la posición
        
    return False #si no encuentra la palabra, retorna False



def prueba():
    print(buscar_palabra("tiempo","Si pasas demasiado tiempo pensando en una cosa, nunca conseguirás hacerla"))
    
if __name__ == "__main__":
    prueba()
        
    
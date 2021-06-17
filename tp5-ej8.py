################
# Giuliano Daniele - @MaiandraGD
# UNRN Andina - Introducción a la Ingeniería en Computación
################



def cifrar(arg="Hola mundo",rot=13):
    """
    Codifica un mensaje(arg) en clave César según un número de rotación(rot), 
    utilizando el alfabeto español. Sólo codifica letras.
        
    """
    
    print(f"El cifrado de '{arg}' con rotación {rot} es:") #mensaje para el usuario
    
    lista = list("abcdefghijklmnñopqrstuvwxyz") #creo lista de letras sobre la cual se usará el rot
    salida = [] #preparo una nueva lista en la que se guardará el cifrado
  
    for letra in arg: #para cada caracter ingresado como argumento
        
        if letra.isalpha(): #solo funciona con letras
            
            if letra.isupper(): #si está en mayusculas:               
                letra_min = letra.lower() #la convierto en minuscula                          
                indice = lista.index(letra_min) +rot #obtengo el indice con la nueva posicion segun rot           
                salida.append(lista[indice % len(lista)].upper()) #le añado la nueva letra a salida, volviendo a mayusc
                
            else:                                     
                indice = lista.index(letra) +rot #obtengo el indice con la nueva posicion segun rot                         
                salida.append(lista[indice % len(lista)]) #le añado la nueva letra a salida
                                       
            continue
        
        salida.append(letra) #añade a la salida el mismo caracter sin modificar, ya que no es una letra
      
    resultado = "".join(salida) #junta la lista de salida como una cadena
    print(resultado) #imprime la cadena resultante ya codificada




def descifrar(arg="Tbxn yhzpb",rot=13):
    
    """
    Decodifica un mensaje(arg) en clave César según un número de rotación(rot), 
    utilizando el alfabeto español. Sólo decodifica letras.
        
    """
    
    print(f"El descifrado de '{arg}' con rotación {rot} es:") #mensaje para el usuario
    
    lista = list("abcdefghijklmnñopqrstuvwxyz") #creo lista de letras sobre la cual se usará el rot
    salida = [] #preparo una nueva lista en la que se guardará el cifrado

    for letra in arg: #para cada caracter ingresado como argumento
        
        if letra.isalpha(): #solo funciona con letras
            
            if letra.isupper(): #si está en mayusculas:               
                letra_min = letra.lower() #la convierto en minuscula                          
                indice = lista.index(letra_min) -rot #obtengo el indice con la nueva posicion segun rot           
                salida.append(lista[indice % len(lista)].upper()) #le añado la nueva letra a salida, volviendo a mayusc                
            
            else:                                     
                indice = lista.index(letra) -rot #obtengo el indice con la nueva posicion segun rot                         
                salida.append(lista[indice % len(lista)]) #le añado la nueva letra a salida    
                
            continue
        
        salida.append(letra) #añade a la salida el mismo caracter sin modificar, ya que no es una letra
      
    resultado = "".join(salida) #junta la lista de salida como una cadena
    print(resultado) #imprime la cadena resultante ya codificada



if __name__ == "__main__":
   
    cifrar()
    print()
    descifrar()




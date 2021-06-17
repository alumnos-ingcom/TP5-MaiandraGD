################
# Giuliano Daniele - @MaiandraGD
# UNRN Andina - Introducción a la Ingeniería en Computación
################


def bin_a_dec(arg):
    """
    Convierte el numero binario (arg) en decimal.
    Retorna False si se ingresan dígitos que no sean 1 o 0.
    """
    
    
    for x in str(arg):                                      #limita la función a digitos 0 y 1 solamente. 
        if x not in "01":
            return False
    
    potencias = [2**x for x in range(len(str(arg)))]        #creo lista de potencias del mismo largo que el número ingresado
    potencias.reverse()                                     #invierto el orden de las potencias
    
    resultado = 0
    
    for i in range(len(str(arg))): #se repetirá la cantidad de cifras del numero
        
        producto = int(potencias[i]) * int(str(arg)[i])
        resultado += producto
                
    return resultado


def dec_a_bin(arg):       
    
    salida = ""
    
    if arg == 0: return 0 #si es cero, retorna cero
    
    while arg > 0:
        salida += str(arg % 2)
        arg = arg // 2
        
    return int(salida[::-1])
        
        

def prueba():
    print("1000 en decimal es",bin_a_dec(1000))
    print("30 en binario es",dec_a_bin(30))

if __name__ == "__main__":
    prueba()
    

                
        
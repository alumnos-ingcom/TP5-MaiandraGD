################
# Giuliano Daniele - @MaiandraGD
# UNRN Andina - Introducción a la Ingeniería en Computación
################


def cadena_balanceada(cadena):
    
    contador = 0 #creo un contador que determinará si la cadena estará balanceada

    for i in cadena:
        
        if i in "([{": #si encuentra un símbolo abierto, suma 1
            contador += 1
            
        elif i in ")]}": #si encuentra un símbolo cerrado, resta 1
            contador -= 1
            
        if contador < 0:
            return False
    
    return contador == 0 #está balanceada sólo si el contador vale cero


if __name__ == "__main__":
    
    cadena_ej = "((()))"
    print(cadena_ej, cadena_balanceada(cadena_ej))


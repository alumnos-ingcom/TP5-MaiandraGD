################
# Giuliano Daniele - @MaiandraGD
# UNRN Andina - Introducción a la Ingeniería en Computación
################

def invertir_mayus():
    texto = input("Ingrese el texto: ")
    salida = ""
    
    for i in texto:
        salida += i.swapcase()
    
    print ("El texto '{}' tiene como salida '{}'".format(texto,salida))
    
if __name__ == "__main__":
    invertir_mayus()
    
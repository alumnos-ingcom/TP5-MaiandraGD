################
# Giuliano Daniele - @MaiandraGD
# UNRN Andina - Introducción a la Ingeniería en Computación
################

def tribonacci(arg):
    
    """
    Permite obtener un término de la secuencia Tribonacci entre 0 y 5000
    """
    
    lista = [0,1,1]
    
    for i,elemento in enumerate(lista):
        
        if len(lista) < 5000:
            termino = elemento + lista[i+1] + lista[i+2]
            lista.append(termino)
        
    return lista[arg]
    

        
def prueba():
    print("El décimo término de la serie Tribonacci es",tribonacci(10))

if __name__ == "__main__":
    prueba()
        
        

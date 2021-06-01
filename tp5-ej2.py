################
# Giuliano Daniele - @MaiandraGD
# UNRN Andina - Introducción a la Ingeniería en Computación
################

def fibonacci(n=0):
        
    """
    Permite obtener el enésimo(n) término de la sucesión Fibonacci
    Si el parámetro ingresado es (-1), se imprimirán los primeros 500 términos.
    """

    salida = [0,1]   
       
    for i in range(500):
        x = salida[-1] + salida [-2]
        salida.append(x)  
    
    
    if n == -1:
        print("Primeros 500 números de la serie Fibonacci:")
        print(salida)
    
    else:
        print(f"El término número {n} es: {salida[n]}")
    
if __name__ == "__main__":
    fibonacci()
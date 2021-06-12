################
# Giuliano Daniele - @MaiandraGD
# UNRN Andina - Introducción a la Ingeniería en Computación
################

def distancia_num(num1, num2):
    
    if (num2>num1):
        return (num1 - num2) * -1
    else:
        return (num1 - num2)
    
if __name__ == "__main__":
    print(distancia_num(2,-2))
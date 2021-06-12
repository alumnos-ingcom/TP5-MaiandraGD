################
# Giuliano Daniele - @MaiandraGD
# UNRN Andina - Introducción a la Ingeniería en Computación
################

def paridad(arg):
    
    if str(arg)[-1] in "24680":
        return True
    else:
        return False
    

if __name__ == "__main__":
    print("Paridad de 12378:",paridad(12378))

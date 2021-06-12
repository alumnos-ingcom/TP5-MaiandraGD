################
# Giuliano Daniele - @MaiandraGD
# UNRN Andina - Introducción a la Ingeniería en Computación
################

def es_capicua(num):
    
    if str(num) == str(num)[::-1]:
        return True
    return False

if __name__ == "__main__":
    print(es_capicua(123))

def CalcularProm(arreglo1, arreglo2): # Definimos la funcion con sus respectivas variables
    promedio = 0 # Valor inicial
    n = len(arreglo1) # Devolver longitud 

    for i in range (n): # Recorremos la funcion 
        promedio += arreglo1[i] * arreglo2[i] 
    return promedio


arreglo1 = [1.5, 2.0, 3.7]
arreglo2 = [0.5, 1.0, 2.2]

resultado = CalcularProm(arreglo1, arreglo2)  # Hacemos llamado de la funcion
print("El producto de estos arreglos es", resultado) # Imprimimos la funcion

def Mover(arreglo): # Hacemos la funcion    
    zeros = [] 
    otros_numeros = [] 

    # Separarmos los ceros de los otros números
    for num in arreglo:
        if num == 0:
            zeros.append(num)
        else:
            otros_numeros.append(num)

    
    arreglo_final = otros_numeros + zeros

    return arreglo_final

arreglo = [1, 0, 3, 0, 5, 0, 2, 0]

arreglo_final = Mover(arreglo)
print("Arreglo original:", arreglo)
print("Arreglo con ceros al final:", arreglo_final)
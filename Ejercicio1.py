def procesar_lista(numeros):
    # 1. Quitar los negativos
    positivos = [n for n in numeros if n >= 0]
    # 2. Quitar duplicados
    sin_repetidos = list(set(positivos))
    # 3. Ordenar
    sin_repetidos.sort()
    return sin_repetidos

if __name__ == "__main__":
    lista = [4, -2, 4, 3, 5, 3, 1, 7, 8]
    print(procesar_lista(lista))

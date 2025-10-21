import re                      
from collections import Counter 

def frecuencia_palabras(ruta_archivo):
    # Abrir y leer el archivo de texto
    with open(ruta_archivo, "r", encoding="utf-8") as f:
        texto = f.read().lower()   

    # Limpiar el texto: quitar signos de puntuación y dejar solo palabras
    palabras = re.findall(r'\b\w+\b', texto)

    # Contar cuántas veces aparece cada palabra
    conteo = Counter(palabras)

    # Mostrar las palabras ordenadas alfabéticamente
    for palabra in sorted(conteo):
        print(palabra, ":", conteo[palabra])

    return conteo


if __name__ == "__main__":

    frecuencia_palabras("Texto.txt")

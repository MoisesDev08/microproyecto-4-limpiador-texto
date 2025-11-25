import sys
import re
from utilidades import analizar_texto

def limpiar_texto(texto):
    limpiar_simbolos = re.sub(r'[^\w,\s]', '  ', texto)
    limpiar_espacios = re.sub(r'\s+', ' ', limpiar_simbolos)
    return limpiar_espacios.strip()
    

if len(sys.argv) > 1:
    archivo = sys.argv[1:]
    try:
        for archivos in archivo:
            
            with open(archivos, "r", encoding="utf-8") as f:
                contenido = f.read()
            resultado = limpiar_texto(contenido)
            if not contenido:
                print("\n")
                print("_" * 50)
                print(f"El archivo {archivos} esta vacio")
                print("_" * 50)
                continue
            resultado_final =                                              analizar_texto(resultado)
            print("\n")
            print("_" * 25)
            print(f"Archivo: {archivos}")
            print("_" * 25)
            print("\n")
            print("_" * 25)
            print(f"Texto limpio:\n {resultado}")
            print("_" * 25)
            print("\n")
            print("_" * 25)  
            print(f"Analisis del texto:\n {resultado_final}")
            print("_" * 25)
            print("\n")
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")            

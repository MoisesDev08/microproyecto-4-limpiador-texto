# Analizador de lista de numeros
def analizar_lista_numeros(lista: list[int]) -> dict:
  """
  Recibe una lista de numeros y devuelve estadisticas basicas.
  
  Parametros: 
  -lista de enteros
  
  Retorna:
  -Diccionario con cantidad, suma, promedio, maximo y minimo.
  """
  return{
    "Cantidad": len(lista),
    "Suma": sum(lista),
    "Maximo": max(lista),
    "Minimo": min(lista),
    "Promedio": sum(lista)/len(lista)  
  }  
  
# Analizador de texto
def analizar_texto(texto) -> dict:
  
  """
  Recibe entrada texto y devuelve conteo de:
  
    - Palabras
    - lineas
    - Caracteres
  """

  palabras = texto.split()
  lineas = texto.split("\n")
  
  return {
    "Caracteres": len(texto),
    "Palabras": len(palabras),
    "Líneas": len(lineas)
  }

# Contador de vocales

def contar_vocales(texto: str) -> dict:
  
  """
  Recibe texto y devuelve conteo de vocales: [a, e, i, o, u]
  
    - Devuelve diccionario con el conteo
  """
  
  texto = texto.lower()
  return {v: texto.count(v) for v in "aeiou"}

# Analizador de lista de decimales

def analizar_lista_decimales(lista: list[float]) -> dict:
  
  """
  Recibe entrada de decimales y devuelve diccionario con parametros:
  - Promedio
  - Cantidad de elementos
  - Suma
  - Minimo
  - Maximo
  """
  
  return {
    "Cantidad": len(lista) if lista else 0,
    "Promedio": round(sum(lista)/len(lista), 2) if lista else 0,
    "Suma total": sum(lista) if lista else 0,
    "Minimo": min(lista) if lista else None,
    "Maximo": max(lista) if lista else None
  }

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import re
import tex as tx


# Función: Limpiar valores numéricos
def limpiar_valor_numerico(valor):

    # Si ya es un número, devolverlo
    if isinstance(valor, (int, float)):
        return float(valor)
    
    # Si es string, procesar
    if isinstance(valor, str):
        try:
            # Eliminar espacios en blanco
            valor = valor.strip()
            
            # Si está vacío o es un guión, devolver NaN
            if valor == '' or valor == '-' or valor == '..':
                return np.nan
            
            # Eliminar puntos (separador de miles)
            valor = valor.replace('.', '')
            
            # Reemplazar coma por punto (separador decimal)
            valor = valor.replace(',', '.')
            
            # Convertir a float
            return float(valor)
            
        except ValueError:
            # Si no se puede convertir, devolver NaN
            return np.nan
    
    # Para cualquier otro tipo, devolver NaN
    return np.nan



# Función: Limpiar el Año
def limpiar_anio(texto):
    if pd.isna(texto): return None
    match = re.search(r'\d{4}', str(texto)) # Busca 4 dígitos seguidos
    if match: return int(match.group(0))
    return None



# Función: Limpiar la Superficie
def limpiar_superficie(texto):
    if pd.isna(texto): return 0.0 # Tu petición: NaN -> 0
    
    # Quitamos los puntos de miles ("14.569" -> "14569")
    # Si no hacemos esto, Python pensará que es 14 coma 569
    texto_limpio = str(texto).replace('.', '')
    
    # Convertimos la coma decimal a punto (por si acaso hubiera decimales reales)
    texto_limpio = texto_limpio.replace(',', '.')
    
    try:
        return float(texto_limpio)
    except:
        return 0.0 # Si falla por texto raro, devuelve 0

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
import re
import tex as tx

# Configuración para mejor visualización
plt.style.use('seaborn-v0_8-darkgrid')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12




def limpiar_valor_numerico(valor):
    """
    Limpia valores numéricos que vienen con formato español.
    
    Parámetros:
    -----------
    valor : str o float
        Valor a limpiar (puede tener punto como separador de miles 
        y coma como separador decimal)
    
    Retorna:
    --------
    float o np.nan
        Valor numérico limpio o NaN si no se puede convertir
    
    Ejemplos:
    ---------
    >>> limpiar_valor_numerico("1.234,56")
    1234.56
    >>> limpiar_valor_numerico("172.587,62")
    172587.62
    """
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


# Probar la función con algunos ejemplos
print("🧪 Pruebas de la función:")
ejemplos = ["172.587,62", "555,86", "3.513,80", "-", "", "123", 123.45]
for ej in ejemplos:
    resultado = limpiar_valor_numerico(ej)
    print(f"  limpiar_valor_numerico({repr(ej)}) = {resultado}")
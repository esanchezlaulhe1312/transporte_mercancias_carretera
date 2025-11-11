
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import re
import tex as tx

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
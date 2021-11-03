# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd
import string

class CDIN:
    
    
    def dqr(data):
        # Lista de variables de la base de datos
        columns = pd.DataFrame(list(data.columns.values), columns=['Nombres'], index=list(data.columns.values))
    
        # Lista de tipos de datos
        data_types = pd.DataFrame(data.dtypes, columns=['Tipo_Dato'])
    
        #Lista de valores perdidos (NaN)
        missing_values = pd.DataFrame(data.isnull().sum(), columns=['Datos_Faltantes'])
    
        #Lista de valores presentes
        present_values = pd.DataFrame(data.count(), columns=['Valores_Presentes'])
    
        #Lista de valores unicos para cada variable
        unique_values = pd.DataFrame(columns=['Num_Valores_Unicos'])
        for col in list(data.columns.values):
            unique_values.loc[col] = [data[col].nunique()]
    
        # Lista de valores mínimos para cada variable
        min_values = pd.DataFrame(columns=['Min'])
        for col in list(data.columns.values):
            try:
                min_values.loc[col]=[data[col].min()]
            except:
                pass
     
        # Lista de valores máximos para cada variable
        max_values = pd.DataFrame(columns=['Max'])
        for col in list(data.columns.values):
            try:
                max_values.loc[col]=[data[col].max()]
            except:
                pass
    
    
        # Columna 'Categórica' que obtenga una valor booleando True cuando mi columna es una variable
        # categóorica y False cuando es numérica
        categorica = pd.DataFrame(columns=['Categorica'])
        for col in list(data.columns.values):
            if data[col].dtype=='object':
                categorica.loc[col] = True
            else:
                categorica.loc[col] = False
    
    
    
        return columns.join(data_types).join(missing_values).join(present_values).join(unique_values).join(min_values).join(max_values).join(categorica)
    
    # Remover signos de puntuación
    def remove_punctuation(x):
        try:
            x=''.join(cf for ch in x if ch not in string.punctuation)
        except:
            pass
        return x 
    
    def remove_digits(x):
        try:
            x=''.join(cf for ch in x if ch not in string.digits)
        except:
            pass
        return x 

    # Remover espacios en blanco
    def remove_blankspace(x):
        try:
            x=''.join(x.split())
        except:
            pass
        return x
    
    # Reemplazar texto
    def replace_text(x, to_replace, replacement):
        try:
            x=x.replace(to_replace, replacement)
        except:
            pass
        return x
    
    # Convertir a mayúsculas
    def uppercase(x):
        try:
            x=x.upper()
        except:
            pass
        return x
    
    # Quitar espacios en blanco izquiera y derecha
    def remove_space(x):
        try:
            x=x.lstrip()
            x=x.rstrip()
        except:
            pass
        return x
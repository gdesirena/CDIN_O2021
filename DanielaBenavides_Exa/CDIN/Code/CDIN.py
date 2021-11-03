# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 08:28:55 2020

@author: Daniela
"""

import pandas as pd
import string

class CDIN:
    
    #%Definicion de la funcion de data quality report
    
    def dqr(data):
    #% Lista de variables(features) de la base de datos
        columns = pd.DataFrame(list(data.columns.values),columns=['Nombres'],index=list(data.columns.values))
    
    #% Lista de tipos de datos
        data_types = pd.DataFrame(data.dtypes, columns = ['Data_Types'])
    
    #% Lista de datos perdidos (missing data)
        missing_values = pd.DataFrame(data.isnull().sum(), columns = ['Missing_Values'])
    
    #% Lista de los datos presentes
        present_values = pd.DataFrame(data.count(), columns =['present_values'])
    
    #% Lista de valores únicos
        unique_values = pd.DataFrame(columns = ['Unique_Values'])
        for col in list(data.columns.values):
            unique_values.loc[col] = [data[col].nunique()]
        
    #% Lista de valores mínimos
        min_values = pd.DataFrame(columns = ['Min'])
        for col in list(data.columns.values):
            try:
                min_values.loc[col] = [data[col].min()]
            except:
                pass
    
    #% Lista de valores máximos
        max_values = pd.DataFrame(columns = ['Max'])
        for col in list(data.columns.values):
            try:
                max_values.loc[col] = [data[col].max()]
            except:
                pass
    
    #% Regresar reporte con la unión de todos los dataframes
        return columns.join(data_types).join(missing_values).join(present_values).join(unique_values).join(min_values).join(max_values)

    #%% Funciones para la limpieza de datos

    # remover signos de puntuación
    def remove_punctuation(x):
        try:
            x = ''.join(ch for ch in x if ch not in string.punctuation)
        except: 
            pass
        return x
    #%% remover dígitos
    def remove_digits(x):
        try:
            x =''.join(ch for ch in x if ch not in string.digits)
        except:
            pass
        return x
    
    #%% remover espacios en blanco
    def remove_whitespace(x):
        try:
            x=''.join(x.split())
        except:
            pass
        return x
    
    #%% reemplazar texto
    def replace_text(x, to_replace, replacement):
        try:
            x= x.replace(to_place, replacement)
        except:
            pass
        return x
    
    #%% convertir a mayúsculas
    def uppercase_text(x):
        try:
            x = x.upper()
        except:
            pass
        return x
    
    #%% convertir a minúsculas
    def lowercase_text(x):
        try:
            x = x.lower()
        except:
            pass
        return x
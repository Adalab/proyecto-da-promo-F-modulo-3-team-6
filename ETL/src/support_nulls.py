#%%
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.impute import KNNImputer
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# %%
def self_incre(df_rawdata):
    ultimo_id = df_rawdata['Employeenumber'].max()
    # Define una variable para el siguiente ID después del último
    siguiente_id = ultimo_id + 1
    # Itera sobre los índices del DataFrame
    for indice in df_rawdata.index:
        if pd.isnull(df_rawdata.at[indice, 'Employeenumber']):  # Verifica si el valor es nulo
            df_rawdata.at[indice, 'Employeenumber'] = siguiente_id  # Asigna el siguiente ID
            siguiente_id += 1  # Incrementa el siguiente ID
    df_rawdata["Employeenumber"] = df_rawdata["Employeenumber"].astype(int)
    # Muestra el DataFrame actualizado
    return df_rawdata
# %%
def nulls_category(dataframe):
    nulls_cat = ['Businesstravel', 'Educationfield', 'Maritalstatus', 'Overtime']
    for columna in nulls_cat:
    # reemplazamos los nulos por el valor Unknown para cada una de las columnas de la lista
        dataframe[columna] = dataframe[columna].fillna("Unknown")
    return dataframe
    


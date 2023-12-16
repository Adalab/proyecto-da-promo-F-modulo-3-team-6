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
    
#%%
def fill_department(df, jobrole, department):
    df['Jobrole'] = df['Jobrole'].apply(lambda x: ' '.join(word.capitalize() for word in x.lower().split()))
    df.loc[df['Jobrole'] == jobrole, 'Department'] = df.loc[df['Jobrole'] == jobrole, 'Department'].fillna(department)
    return df 
#%%
def iterative_imputer(dataframe):
    # instanciamos las clases										
    imputer_iterative = IterativeImputer(max_iter = 20, random_state = 42)			
    # ajustamos y tranformamos los datos										
    imputer_iterative_imputed = imputer_iterative.fit_transform(dataframe[['Dailyrate', 'Distancefromhome', 'Monthlyincome', 'Performancerating','Totalworkingyears', 'Worklifebalance', 'Hourlyrate']])
    dataframe[['Dailyrate_ITE', 'Distancefromhome_ITE', 'Monthlyincome_ITE', 'Performancerating_ITE','Totalworkingyears_ITE', 'Worklifebalance_ITE', 'Hourlyrate_ITE']] = imputer_iterative_imputed
    return dataframe
#%%
def knn_imputer(dataframe):
    # instanciamos la clase del KNNImputer
    imputer_knn = KNNImputer(n_neighbors = 5)
    # ajustamos y transformamos los datos
    imputer_knn_imputed = imputer_knn.fit_transform(dataframe[['Dailyrate', 'Distancefromhome', 'Monthlyincome', 'Performancerating','Totalworkingyears', 'Worklifebalance', 'Hourlyrate']])
    dataframe[['Dailyrate_KNN', 'Distancefromhome_KNN', 'Monthlyincome_KNN', 'Performancerating_KNN','Totalworkingyears_KNN', 'Worklifebalance_KNN', 'Hourlyrate_KNN']] = imputer_knn_imputed
    return dataframe
#%%
def rearrange(dataframe):
    dataframe.drop(['Dailyrate', 'Dailyrate_ITE', 'Distancefromhome', 'Distancefromhome_ITE', 'Monthlyincome', 'Monthlyincome_ITE', 'Performancerating', 'Performancerating_ITE', 'Totalworkingyears', 'Totalworkingyears_ITE', 'Worklifebalance', 'Worklifebalance_ITE', 'Hourlyrate', 'Hourlyrate_ITE'], axis = 1, inplace = True)
    # ahora vamos a cambiar el nombre de las columnas que quedaron para que tengan el mismo nombre de origen
    nuevo_nombre = {"Dailyrate_KNN": "Dailyrate",  'Distancefromhome_KNN': "Distancefromhome", "Monthlyincome_KNN": "Monthlyincome", "Performancerating_KNN": "Performancerating","Totalworkingyears_KNN": "Totalworkingyears", "Worklifebalance_KNN": "Worklifebalance", "Hourlyrate_KNN":"Hourlyrate"}
    dataframe.rename(columns = nuevo_nombre, inplace = True)


# %%

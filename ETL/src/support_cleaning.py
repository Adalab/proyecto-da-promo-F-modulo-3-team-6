#%% 
#!pip install word2number
import pandas as pd
from word2number import w2n
import numpy as np

#%%
def capitalize_col(dataframe):
    new_columns={columna: columna.capitalize() for columna in dataframe.columns} 
    dataframe_capitalize_done = dataframe.rename(columns = new_columns, inplace = True)
    return dataframe_capitalize_done

# %%
def drop_duplicated(dataframe, column):
    # Mantener el último duplicado y conservar los NaN
    dataframe_drop_dup = dataframe[~dataframe[column].duplicated(keep='last') | dataframe[column].isnull()]
    return dataframe_drop_dup

# %%
def drop_col(dataframe_drop_dup, list_drop):
    dataframe_drop_dup.drop(list_drop, axis=1 , inplace=True, errors='raise')
    return dataframe_drop_dup

#%%
def renaming_remotework(dataframe):
    dict_map = {"0": "No", "False": "No", "1": "Yes", "True": "Yes", "Yes": "Yes"}
    dataframe["Remotework"] = dataframe["Remotework"].map(dict_map)
    return dataframe

#%%
def gender_changed(dataframe):
    dataframe['Gender'] = dataframe['Gender'].astype(str)
    dataframe['Gender'] = dataframe['Gender'].replace('0', "Male")
    dataframe['Gender'] = dataframe['Gender'].replace('1', "Female")
    return dataframe


#%%
#Función que transforma las palabras (en inglés) y strings de números ('54') a integers
def transform_to_number(age):
    #Hemos puesto try y except porque al hacerlo una vez funcionaba una la segunda vez daba error
    try:
        return w2n.word_to_num(age)
    #Con este except le decimos que devuelva el integer sin cambiarlo
    except:
        return age 

#%% 
def title_jobrole(dataframe):
    dataframe['Jobrole'] = dataframe['Jobrole'].str.title()
    return dataframe

#%%
def select_dig_env(dataframe):
    dataframe["Environmentsatisfaction"] = dataframe["Environmentsatisfaction"].astype(str).str.replace(r'(\d)\d', r'\1', regex=True).astype(int)
    return dataframe
#%%
def transform_salary(dailyrate):
    try:
        return float(dailyrate.replace("$","").replace(",",".").strip())
    except:
        
        return dailyrate
#%%
def labels_satisfaction(dataframe,col):
    dict_map = {1: "Not Satisfied", 2: "Somewhat Satisfied", 3: "Satisfied", 4: "Very Satisfied"}
    
    try: 
        dataframe[col] = dataframe[col].map(dict_map)
        #dataframe_rawdata["Jobsatisfaction"].head(5)
        return dataframe[col]
    except: 
        return col 
    

# %%
def labels_joblevel(df,col):
    dict_job = {
1: "Entry-level",
2: "Junior",
3: "Mid-level",
4: "Senior",
5: "Executive"
}
    try: 
        df[col] = df[col].map(dict_job)
        #dataframe["Jobsatisfaction"].head(5)
        return df[col]
    except: 
        return col
#%%
def marital (dataframe):
    dataframe['Maritalstatus'] = dataframe['Maritalstatus'].str.title()
    dataframe['Maritalstatus'] = dataframe['Maritalstatus'].replace('Marreid', "Married") 
    return dataframe

#%%
def comma_substitution(cadena):
    try:
        return float(cadena.replace(",", "."))
    except:
        return np.nan
    

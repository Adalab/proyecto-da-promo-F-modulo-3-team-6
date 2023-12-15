#%% 
import pandas as pd

#%%
def capitalize_col(dataframe):
    new_columns={columna: columna.capitalize() for columna in dataframe.columns} 
    df_capitalize_done = dataframe.rename(columns = new_columns, inplace = True)
    return df_capitalize_done

# %%
def drop_duplicated(dataframe, column):
    # Mantener el último duplicado y conservar los NaN
    df_drop_dup = dataframe[~dataframe[column].duplicated(keep='last') | dataframe[column].isnull()]
    return df_drop_dup

# %%
def drop_col(dataframe, list_drop):
    df_drop_col = dataframe.drop(list_drop, axis=1 , inplace=True, errors='raise')
    return df_drop_col

#%%
def renaming_remotework(dataframe):
    dict_map = {"0": "No", "False": "No", "1": "Yes", "True": "Yes", "Yes": "Yes"}
    df_rere = dataframe["Remotework"] = dataframe["Remotework"].map(dict_map)
    return df_rere


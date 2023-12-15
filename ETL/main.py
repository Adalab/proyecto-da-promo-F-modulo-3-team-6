#%%
import pandas as pd
from src import support_exploration as sex
from src import support_cleaning as scl
from src import support_DDBB as sdb
from src import support_AB_testing as sab

pd.set_option('display.max_columns', None) # para poder visualizar todas las columnas de los DataFrames

# %%
df = pd.read_csv("data/HR RAW DATA.csv", index_col=0)
# %%
sex.exploracion_csv(df)

# %%
scl.capitalize_col(df)

#%%
df_noduplicated = scl.drop_duplicated(df, 'Employeenumber')

#%% 
df_drop_col = scl.drop_col(df_noduplicated,["Over18", "Standardhours", "Yearsincurrentrole", "Employeecount", "Sameasmonthlyincome", "Salary", "Numberchildren", "Roledepartament"])

#%%
df_re_re = scl.renaming_remotework(df_drop_col)
df_re_re.head(10)
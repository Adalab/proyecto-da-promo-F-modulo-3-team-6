#%%
import pandas as pd
from word2number import w2n
from src import support_exploration as sex
from src import support_cleaning as scl
from src import support_nulls as snu
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

#%%
df_gender = scl.gender_changed(df_re_re)

#%%
df_gender["Age"] = df_gender["Age"].apply(scl.transform_to_number)

# %%
scl.title_jobrole(df_gender)

#%%
scl.select_dig_env(df_gender)

#%%
df_gender["Dailyrate"]= df_gender["Dailyrate"].apply(scl.transform_salary)


#%%
columns_to_modify = ["Jobsatisfaction", "Relationshipsatisfaction", "Environmentsatisfaction"]
for column in columns_to_modify:
    df_gender[column] = scl.labels_satisfaction(df_gender,column)

#%%
df_gender["Joblevel"] = scl.labels_joblevel(df_gender,"Joblevel")

#%%
df_format=scl.marital(df_gender)

#%%
columns_to_modify=["Worklifebalance", "Monthlyincome", "Performancerating", "Totalworkingyears","Employeenumber"]
for column in columns_to_modify:
    df_format[column] = df_format[column].apply(scl.comma_substitution)
# %%
df_self=snu.self_incre(df_format)

#%%
df_category=snu.nulls_category(df_self)
   

#%%
import pandas as pd
from word2number import w2n
from src import support_exploration as sex
from src import support_cleaning as scl
from src import support_nulls as snu
from src import support_DDBB as sdb
from src import support_AB_testing as sab

pd.set_option('display.max_columns', None) # para poder visualizar todas las columnas de los DataFrames
df = pd.read_csv("data/HR RAW DATA.csv", index_col=0)
# %%
sex.exploracion_csv(df)
scl.capitalize_col(df)
#%%
df_noduplicated = scl.drop_duplicated(df, 'Employeenumber')
df_drop_col = scl.drop_col(df_noduplicated,["Over18", "Standardhours", "Yearsincurrentrole", "Employeecount", "Sameasmonthlyincome", "Salary", "Numberchildren", "Roledepartament"])
df_re_re = scl.renaming_remotework(df_drop_col)
df_gender = scl.gender_changed(df_re_re)
df_gender["Age"] = df_gender["Age"].apply(scl.transform_to_number)

scl.title_jobrole(df_gender)
scl.select_dig_env(df_gender)

df_gender["Dailyrate"]= df_gender["Dailyrate"].apply(scl.transform_salary)

columns_to_modify = ["Jobsatisfaction", "Relationshipsatisfaction", "Environmentsatisfaction"]
for column in columns_to_modify:
    df_gender[column] = scl.labels_satisfaction(df_gender,column)

#%%
df_gender["Joblevel"] = scl.labels_joblevel(df_gender,"Joblevel")

df_format=scl.marital(df_gender)

columns_to_modify=["Worklifebalance", "Monthlyincome", "Performancerating", "Totalworkingyears","Employeenumber"]
for column in columns_to_modify:
    df_format[column] = df_format[column].apply(scl.comma_substitution)
#%%
df_format["Distancefromhome"] = df_format["Distancefromhome"].apply(scl.negative_to_null)
df_format["Hourlyrate"] = df_format["Hourlyrate"].apply(scl.not_available_to_null)
# %%
df_self=snu.self_incre(df_format)

#%%
df_category=snu.nulls_category(df_self)
    
#%%
# Uso de la función fill_department para reemplazar los valores faltantes en 'Department'
df_category = snu.fill_department(df_category, 'Research Director', 'Research & Development')
df_category = snu.fill_department(df_category, 'Healthcare Representative', 'Research & Development')
df_category = snu.fill_department(df_category, 'Laboratory Technician', 'Research & Development')
df_category = snu.fill_department(df_category, 'Manufacturing Director', 'Research & Development')
df_category = snu.fill_department(df_category, 'Research Scientist', 'Research & Development')
df_category = snu.fill_department(df_category, 'Sales Executive', 'Sales')
df_category = snu.fill_department(df_category, 'Sales Representative', 'Sales')
df_category = snu.fill_department(df_category, 'Human Resources', 'Human Resources')
df_category = snu.fill_department(df_category, 'Manager', 'Unknown')

# %%
df_final = df_category.copy()
snu.iterative_imputer(df_final)
snu.knn_imputer(df_final)
df_final.describe()[['Dailyrate', 'Dailyrate_ITE', 'Dailyrate_KNN', 'Distancefromhome', 'Distancefromhome_ITE','Distancefromhome_KNN', 'Monthlyincome', 'Monthlyincome_ITE','Monthlyincome_KNN','Performancerating','Performancerating_ITE','Performancerating_KNN','Totalworkingyears','Totalworkingyears_ITE','Totalworkingyears_KNN', 'Worklifebalance', 'Worklifebalance_ITE','Worklifebalance_KNN','Hourlyrate','Hourlyrate_ITE','Hourlyrate_KNN']]
#Hemos seleccionado el método KNN Imputer ya que los resultados son más precisos.

#%%
snu.rearrange(df_final)
# %%
#df_final.to_csv("../Data/raw_data_final.csv")
#%%
import pandas as pd
import os
from dotenv import load_dotenv
from word2number import w2n
from src import support_exploration as sex
from src import support_cleaning as scl
from src import support_nulls as snu
from src import support_DDBB as sdb
from src import support_AB_testing as sab
from src import queries_creacion_tablas as squ

load_dotenv("src/.env")

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
df_definitive = scl.labels_jobinvolv(df_final)
df_definitive.head()


#df_definitive.to_csv("../data/raw_data_final.csv")

#%%
our_password = os.getenv("our_password")  
name_ddbb = os.getenv("name_ddbb") 

# Creación base de datos
sdb.creacion_bbdd_tablas(squ.query_creacion_bbdd, our_password, name_ddbb)
# Creación de las tablas 
sdb.creacion_bbdd_tablas(squ.query_tabla_personal_data, our_password)
sdb.creacion_bbdd_tablas(squ.query_tabla_laboral_data, our_password)
sdb.creacion_bbdd_tablas(squ.query_tabla_laboral_life, our_password)
sdb.creacion_bbdd_tablas(squ.query_tabla_economic_data, our_password)
sdb.creacion_bbdd_tablas(squ.query_tabla_satisfaction, our_password)

#%%
data_table1 = list((zip(df_definitive["Employeenumber"].values, df_definitive["Age"].values, df_definitive["Gender"].values, df_definitive["Maritalstatus"].values,df_definitive["Datebirth"].values)))
data_table1 = sdb.change_to_float(data_table1)
#%%
df_definitive.rename(columns={"Yearswithcurrmanager": "Yearswithcurrentmanager"}, inplace=True)
data_table2 = list((zip(df_definitive["Joblevel"].values, df_definitive["Jobrole"].values, df_definitive["Businesstravel"].values, df_definitive["Department"].values, df_definitive["Overtime"].values, df_definitive["Distancefromhome"].values, df_definitive["Yearssincelastpromotion"].values,df_definitive["Yearsatcompany"].values, df_definitive["Yearswithcurrentmanager"].values,df_definitive["Remotework"].values, df_definitive["Trainingtimeslastyear"].values,df_definitive["Attrition"].values)))
data_table2 = sdb.change_to_float(data_table2)
#%%
data_table2b = list((zip(df_definitive["Numcompaniesworked"].values, df_definitive["Totalworkingyears"].values, df_definitive["Education"].values, df_definitive["Educationfield"].values)))
data_table2b = sdb.change_to_float(data_table2b)
#%%
data_table3 = list((zip(df_definitive["Monthlyrate"].values, df_definitive["Percentsalaryhike"].values, df_definitive["Stockoptionlevel"].values, df_definitive["Dailyrate"].values,df_definitive["Monthlyincome"].values,df_definitive["Hourlyrate"].values,)))
data_table3 = sdb.change_to_float(data_table3)
#%%
data_table4 = list((zip(df_definitive["Environmentsatisfaction"].values, df_definitive["Jobinvolvement"].values, df_definitive["Jobsatisfaction"].values, df_definitive["Relationshipsatisfaction"].values,df_definitive["Performancerating"].values, df_definitive["Worklifebalance"].values)))
data_table4 = sdb.change_to_float(data_table4)
#%%
# Insertar los datos en las tablas
#df_definitive[["Employeenumber", "Age", "Gender", "Maritalstatus", "Datebirth"]] = df_definitive[["Employeenumber", "Age", "Gender", "Maritalstatus", "Datebirth"]].applymap(bss.convertir_lista)
sdb.insert_data(squ.query_insert_table1, our_password, name_ddbb, data_table1)
#%%
sdb.insert_data(squ.query_insert_table2, our_password, name_ddbb, data_table2)
#%%
sdb.insert_data(squ.query_insert_table2b, our_password, name_ddbb, data_table2b)
sdb.insert_data(squ.query_insert_table3, our_password, name_ddbb, data_table3)
#%%
sdb.insert_data(squ.query_insert_table4, our_password, name_ddbb, data_table4)

# %%

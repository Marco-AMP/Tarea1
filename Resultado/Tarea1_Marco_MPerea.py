import pandas as pd
poblacion=pd.read_csv('POB_TOT.csv', header=0)
poblacionnew=poblacion.iloc[:,4:67]
pais= poblacion.iloc[:,0]
poblacionnew=poblacionnew.assign(CountryName=pais)
print(poblacionnew)
poblacionnew.to_csv('New_POB_TOT')
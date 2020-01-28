import pandas as pd
import numpy as np

df2019=pd.read_csv("EU2019_BE_EndgErg_Wahlbezirke.csv",
                    encoding="cp1252", delimiter=";")

df2019=df2019[["Wähler", "CDU", "SPD", "GRÜNE"]]
#how- er zeigt nur die zeilen wo nur Nan ist
df2019=df2019.dropna(how="all")
#print(df2019.dtypes)
nums=df2019["Wähler"].str.isnumeric()
print(df2019[~nums])

df2019["Wähler"]=df2019["Wähler"].str.replace(" ","")
nums=df2019["Wähler"].str.isnumeric()
print(df2019[~nums])

df2019=df2019.applymap(int)
print(df2019.dtypes)

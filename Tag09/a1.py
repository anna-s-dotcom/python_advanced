import pandas as pd
import numpy as np

# with open("state-abbrevs.csv") as file:
#     for line in file:
#         print(line)
#
csv1 = pd.read_csv("state-abbrevs.csv")

print("csv1")
print(csv1)

csv2=pd.read_csv("state-areas.csv")

print("csv2")
print(csv2)

csv3=pd.read_csv("state-population.csv")
print("csv3")
print(csv3)

dfc1=pd.concat([csv1,csv2,csv3],axis=0, sort=False)
print(dfc1)

# sofort beim einlesen der Datei, index sollte state sein
df2=pd.read_csv("state-abbrevs.csv").set_index("state")
df3=pd.read_csv("state-areas.csv", index_col="state")
print(df2)
print("head")
print(df2.head())

#isna=is not a number
dfc=pd.concat([df2,df3],axis=1, sort=False)
print(dfc.isna().any())
print(dfc[dfc["abbreviation"].isna()])
#den fehlenden Element ergänzen- hier Puerto Rico
dfc.loc["Puerto Rico", "abbreviation"]="PR"
print()
print(dfc.loc["Puerto Rico"]["abbreviation"])

print()
print(dfc.loc["Puerto Rico"])
print()
print(dfc.tail())

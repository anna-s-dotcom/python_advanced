import pandas as pd


# csv1 = pd.read_csv("jena1.csv").set_index("statistischer_Bezirk_Nr")
# csv2 = pd.read_csv("jena2.csv").set_index("statistischer_Bezirk_Nr")
#
# print(csv1.head())
# print(csv2.head())
#
# dfc=pd.concat([csv1,csv2],axis=0, sort=False)
# print(dfc)
#
# for i in dfc:
#     print(i)



#  Unnamed: 0 statistischer_Bezirk_Name  ...  Einheit    Wert
# Unnamed: 0 statistischer_Bezirk_Name  ...  Einheit    Wert
df1 = pd.read_csv("jena1.csv",index_col=0)
df2 = pd.read_csv("jena2.csv",index_col=0)

print((df1.columns==df2.columns).all())


dfc=pd.concat([df1,df2])
dfc=dfc.sort_index()

# print(dfc)


df1.append()

import pandas as pd
import numpy as np

df1=pd.DataFrame(np.arange(9).reshape(3,3), columns=["A", "B", "C"], index=[2,3,4])

df2=pd.DataFrame(np.arange(9,15).reshape(3,2),columns=["C", "D"])

print(df1)
print()
print(df2)

print("nichts")
dfc1=pd.concat([df1,df2])
#ignore index- löscht den alten index und vergibt einen neuen
print("False")
dfc1=pd.concat([df1,df2], axis=0, sort=False, ignore_index=True)

print(dfc1)
print("True")
dfc2=pd.concat([df1,df2],axis=0, sort=True)

print(dfc2)

#nur spalten,die in beiden daten frames vorkommen
print("Join")
dfc3=pd.concat([df1,df2], axis=0, sort=False, join="inner")
print(dfc3)


print("Fillna")
dfc4=pd.concat([df1,df2], axis=0, sort=False).fillna(0)
print(dfc4)



print("Achse 1")
dfc5=pd.concat([df1,df2], axis=1, sort=False)
print(dfc5)

#die spalte auswählen und nach ihr daten frames indexieren

print(dfc5.set_index("B"))

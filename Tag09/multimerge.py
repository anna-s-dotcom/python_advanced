import pandas as pd

df1=pd.DataFrame(columns=["dep", "nr","sal"])
df1["dep"]=["PR", "Dev", "Acc"]
df1["nr"]=[1,2,4]
df1["sal"]=[50,30,120]

df2=pd.DataFrame(columns=["name", "dept"])
df2["name"]=["Alex", "Anna", "Bella", "Björn"]
df2["dept"]=["PR", "PR", "Dev", "Acc"]

print(df1)
print()
print(df2)

# dfm=pd.merge(df1,df2, left_on="dep", right_on="dept")
# print(dfm)


dfm=pd.merge(df1, df2
                validate="1:m",
                left_on="dep",
                right_on="dept").drop("dep",axis=1)
print(dfm)

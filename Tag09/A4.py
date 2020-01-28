import pandas as pd

#auf fehler zu überprüfen
df1 = pd.read_csv("state-abbrevs.csv")
df2 = pd.read_csv("state-areas.csv")
df2 = pd.read_csv("state-areas.csv")



dfm=pd.merge(df1, df2,
                validate="1:m",
                left_on="dep",
                right_on="state").drop("state",axis=1)
print(dfm)

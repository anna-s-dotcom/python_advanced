import pandas as pd

#zusammenführen ohne neuen Index
df1 = pd.read_csv("state-abbrevs.csv")
df2 = pd.read_csv("state-areas.csv")

# print(df1)
# print(df2)

#puerto rico finden, mit dem Wert None
#wenn kein outer dann inner- also wenn die werte sich überschreiten
#true- ist falsch
#
dc=pd.merge(df1,df2, how="outer")
print(dc)
#any -spalten und zeilen, mindestens eins
#noch all
print(dc.isna().any())
print(dc.isna()["abbreviation"])
print(dc[dc.isna()["abbreviation"]])


dc_clean=dc.fillna("PR")

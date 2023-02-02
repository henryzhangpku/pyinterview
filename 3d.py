import pandas as pd
import numpy as np

DATENAME = 'DATE'
IDNAME = 'ID'
DIMPREFIX = 'DIM'
DIM3NAME = DIMPREFIX + '3'
DATANAME = 'DATA'

col1 = pd.DataFrame(np.random.randn(5, 3), index=pd.date_range(start='1/1/2023', periods=5),
                    columns=["AAPL", "TLSA", "MSFT"])
col2 = pd.DataFrame(np.random.randn(5, 3), index=pd.date_range(start='1/1/2023', periods=5),
                    columns=["AAPL", "TLSA", "MSFT"])
data = [col1, col2]


def from_2d(data):
    all_dfs = []
    for i, col in enumerate(data):
        mi = pd.MultiIndex.from_product(
            [col.columns, [str(i)]], names=[IDNAME, DIM3NAME])
        all_dfs.append(col.reindex(columns=mi, level=0))

    df = pd.concat(all_dfs, axis=1)
    df.sort_index(axis=0, inplace=True)
    df.sort_index(axis=1, inplace=True)
    df.index.name = DATENAME
    return df


df = from_2d(data)
df = df[df.notnull()]
print(df)
print(df['AAPL'].idxmax())
df = df.stack().stack()
#print(df)
df=df.to_frame()
print(df)
df = df.reset_index()
df=df.set_index(DATENAME)
#df=df.unstack()
print(df)
#df2=df.groupby("ID").apply(sum)
#print(df2)
df2=df.unstack()
print(df.unstack())
# print(df.unstack().unstack())

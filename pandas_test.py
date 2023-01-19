import pandas as pd
import datetime
# df=pd.DataFrame(index=[], columns=['timestamp','A','B','C']).fillna(0)
# df['timestamp']=pd.to_datetime(df['timestamp'])
# df=df.set_index(['timestamp'])
# print(df)
# t='20200215010304'
# df.loc[t,'A']= 3 #[3,4,5]
# df=df.fillna(0)
# print(df)

# t='20200103010304'
# df.loc[t,'B']= 5 #[3,4,5]
# df=df.fillna(0)
# print(df)

# t='20200103010304'
# df.loc[t,'C']= 1 #[3,4,5]
# df=df.fillna(0)
# print(df)
# df['D']=0 #df['A']+df['B']
# print(df)

# agg=df.resample('H').sum()

# print(agg)
class PyLogger:
	def __init__(self):
		self.df=pd.DataFrame(index=[], columns=['timestamp','A','B','C']).fillna(0)
		self.df['timestamp']=pd.to_datetime(self.df['timestamp'])
		self.df=self.df.set_index(['timestamp'])

	def set(self, t, c, v):
		self.df.loc[t,c]=v

	def get(self,t,c):
		return self.df.loc[t,c]

	def agg(self, start_time, end_time , freq):
		agg=self.df.resample(freq).sum()
		print(agg)
		return agg.loc[start_time:end_time]

o=PyLogger()

o.set("20220101123105", 'A', 1)
o.set("20220102123105", 'B', 2)
o.set("20220103123105", 'C', 3)

print(o.get("20220101123105", 'A'))
print(o.agg("20220101","20220103", '60min'))


def tracking_in_time_keywords(kw_list):pytrends = TrendReq(hl='country', tz=0)
future_dataframe={}c=1
for i in range(len(kw_list)):
if i%2==0:
try:
print("Requesting ",str(kw_list[i]))pytrends.build_payload(kw_list[i], cat=kw_list[i+1],timeframe=dates, geo='country', gprop='')future_dataframe[c]=pytrends.interest_over_time()
future_dataframe[c].drop(['isPartial'], axis=1,inplace=True)
c+=1
result = pd.concat(future_dataframe, axis=1)# this is for intense API requesting
secs=int(random.randrange(10, 50))
print("Sleeping {} seconds before requesting ".format(secs), str(kw_list[i]))timer.sleep(secs)
print("Done")except:print("***","\n","Error with ",kw_list[i],"or not enough trending percentaje","\n","***")df1=result.unstack(level=-1)
df2=pd.DataFrame(df1)return df2

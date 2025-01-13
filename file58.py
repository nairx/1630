import pandas as pd
score = [20,27,32]
series = pd.Series(score) #using list
series = pd.Series(score,index=["John","Cathy","Ria"])
print(series)
print(series["John"])
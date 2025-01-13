import pandas as pd 
marks = {'Suman':[20],"Nikhil":[34],"Srikala":[67]}
# myseries = pd.DataFrame(marks)
myseries = pd.DataFrame(marks,index=['score'])
print(myseries)
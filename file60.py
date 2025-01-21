import pandas as pd 
marks = {'Suman':[20,56],"Nikhil":[34,23],"Srikala":[67,78]}
# myseries = pd.DataFrame(marks)
myseries = pd.DataFrame(marks,index=['Maths','Science'])
print(myseries)
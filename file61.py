import pandas as pd 
ds = {
    'name':['Akhil','Auzaan','Srikala'],
    'score':[67,78,93]
}
# d = pd.DataFrame(ds)
d = pd.DataFrame(ds,index=['Maths','Science','English'])
d.to_csv('marks.csv')
print(d)
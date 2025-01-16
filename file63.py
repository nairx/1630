import pandas as pd 
data = {
    "Maths":{"Suman":80,"John":70,"Cathy":80},
    "Science":{"Suman":60,"John":90,"Cathy":40},
    "English":{"Suman":70,"John":50,"Cathy":70},
    "Telugu":{"Suman":80,"John":70,"Cathy":80},
    "HIndi":{"Suman":60,"John":90,"Cathy":40},
    "Spanish":{"Suman":70,"John":50,"Cathy":70},
    "French":{"Suman":80,"John":70,"Cathy":80},
}
df = pd.DataFrame(data)
print(df)
df.to_csv("Score.csv",index=False)

import pandas as pd
data = {"Name": ["Selva", "Gopi", "Ganesh"], "Age": [19, 20, 19]}
df = pd.DataFrame(data, index=[1, 2, 3], dtype= int)
print(df)
print(df.Age.mean())

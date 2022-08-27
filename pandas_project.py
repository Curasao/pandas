
import pandas as pd
DataF = {
'fruits' : ["apple", "peach", "orange", "bannana", "melon"],
'vegetable': ["tomato", "cucumber", "beat", "garlic", "celary"]
}
df = pd.DataFrame(DataF)
print('DataFrame: \n', df)
with open('csv_data.txt', 'w') as csv_file:
    df.to_csv(path_or_buf=csv_file)

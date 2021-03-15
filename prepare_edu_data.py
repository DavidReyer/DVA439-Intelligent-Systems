import pandas as pd

dataset = pd.read_csv('datasets/1/xAPI-Edu-Data.csv')

def map_function(x):
    if x < 20:
        return 20
    if 20 < x < 40:
        return 40
    if 40 < x < 60:
        return 60
    if 60 < x < 80:
        return 80
    return 100

dataset["raisedhands"] = dataset["raisedhands"].apply(map_function)
dataset["VisITedResources"] = dataset["VisITedResources"].apply(map_function)
dataset["AnnouncementsView"] = dataset["AnnouncementsView"].apply(map_function)
dataset["Discussion"] = dataset["Discussion"].apply(map_function)

columns = list(dataset.columns)
columns += [columns.pop(columns.index('Topic'))]
columns.pop(columns.index('Class'))

dataset.to_csv('datasets/1/xAPI-Edu-Data-categorized.csv', columns=columns, index=False)

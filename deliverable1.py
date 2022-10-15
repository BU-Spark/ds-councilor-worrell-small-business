import pandas as pd

def read_csv(filepath):
    df = pd.read_csv(filepath)
    return df

df = read_csv("/Users/davegodfrey/Desktop/CS Degree/Computer Science/CS 506/homework-1-DaveG77/train.csv")
df.describe()
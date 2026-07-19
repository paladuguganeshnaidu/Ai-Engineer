import pandas as pd

file_path = r"C:/Users/ganes/.cache/kagglehub/datasets/bwandowando/cloud-vendors-and-related-tweets-dataset/versions/2/0423_to_0703_CloudProvidersTweets.csv.gzip"

df = pd.read_csv(file_path, compression="gzip")

print(df.columns.tolist())
print(df.head())
print(df.info())
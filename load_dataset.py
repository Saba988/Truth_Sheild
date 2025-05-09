import pandas as pd

# Updated path to the dataset
dataset_path = "C:/Users/FCC/.cache/kagglehub/datasets/clmentbisaillon/fake-and-real-news-dataset/versions/1/Fake.csv"

# Load the dataset into a pandas DataFrame
df = pd.read_csv(dataset_path)

# Display the first few rows of the dataset
print(df.head())

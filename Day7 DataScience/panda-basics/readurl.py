import pandas as pd

url = "https://media.geeksforgeeks.org/wp-content/uploads/20241121154629307916/people_data.csv"
df = pd.read_csv(url)
print(df)
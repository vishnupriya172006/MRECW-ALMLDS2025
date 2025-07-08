import pandas as pd

# Sample data stored in a multi-line string
data = """totalbill_tip, sex:smoker, day_time, size
16.99, 1.01:Female|No, Sun, Dinner, 2
10.34, 1.66, Male, No|Sun:Dinner, 3
21.01:3.5_Male, No:Sun, Dinner, 3
23.68, 3.31, Male|No, Sun_Dinner, 2
24.59:3.61, Female_No, Sun, Dinner, 4
25.29, 4.71|Male, No:Sun, Dinner, 4"""

# Save the data to a CSV file
# with open("sample.csv", "w") as file:
#     file.write(data)
# print(data)

# Load the CSV file using pandas with multiple delimiters
df = pd.read_csv('sample.csv',
                 sep='[:, |_]',  # Define the delimiters
                 engine='python')  # Use Python engine for regex separators
print(df)

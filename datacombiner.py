import pandas as pd
import os
import re
import sys

# Get the directory from the command-line argument (if provided)
if len(sys.argv) > 1:
    directory = sys.argv[1]
else:
    directory = './'

heart_file = None
oxygen_file = None
hrbrc_file = None

# Get a list of files in the current directory
files = os.listdir(directory)

# Loop through the files and find the first one that contains each of the specified strings
for file in files:
    if "heart" in file and not heart_file:
        heart_file = file
    elif "oxygen" in file and not oxygen_file:
        oxygen_file = file
    elif "datalog" in file and not hrbrc_file:
        hrbrc_file = file
    

print("Heart rate file:", heart_file)
print("Oxygen level file:", oxygen_file)
print("HRBRC file:", hrbrc_file)

df1=pd.read_csv(directory+heart_file, header=1, na_values=[''], index_col=False)
df2=pd.read_csv(directory+oxygen_file, header=1, na_values=[''], index_col=False)
#assume the first row of data has sensor boot data and should be thrown out
df3=pd.read_csv(hrbrc_file, header=0, skiprows=[1])

# Convert the date column to a datetime type
df1['DateTime'] = pd.to_datetime(df1['com.samsung.health.heart_rate.end_time'])
df2['DateTime'] = pd.to_datetime(df2['com.samsung.health.oxygen_saturation.end_time'])
df3['DateTime'] = pd.to_datetime(df3['Year'].astype(str)+'-'+df3['Month'].astype(str)+'-'+df3['Day'].astype(str)+', '+df3['Hour'].astype(str)+':'+df3['Minute'].astype(str)+':'+df3['Second'].astype(str))
#df3['DateTime'] = pd.to_datetime(df3['Date']+ ' ' + df3[' Time'])

# Perform an outer join on date1 and date2
combined_df = pd.merge(df1, df2, left_on='DateTime', right_on='DateTime', how='outer')
# Perform an outer join on date1 and date2
combined_df = pd.merge(combined_df, df3, left_on='DateTime', right_on='DateTime', how='outer')

# Sort the combined dataframe by combodate
combined_df = combined_df.sort_values(by="DateTime")

# Write the sorted dataframe to a new CSV file
combined_df.to_csv("combined_sorted.csv", index=False)
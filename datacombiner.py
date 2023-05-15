import pandas as pd
import os
import re
import sys
import argparse

# Create the argument parser
parser = argparse.ArgumentParser()

# Add the directory argument with default as the current directory
parser.add_argument('-d', '--directory', default='./', help='Directory path')

# Add the file arguments with default values based on filenames containing specific strings
parser.add_argument('-f1', '--file1', default=[file for file in os.listdir() if 'heart' in file][0], help='Heart Sensor Data file path')
parser.add_argument('-f2', '--file2', default=[file for file in os.listdir() if 'oxygen' in file][0], help='Oxygen Sensor Data file path')
parser.add_argument('-f3', '--file3', default=[file for file in os.listdir() if 'datalog' in file][0], help='Squirrel Crack Sensor Data file path')

# Parse the command-line arguments
args = parser.parse_args()

# Access the values of the directory and file arguments
directory = args.directory
heart_file = args.file1
oxygen_file = args.file2
hrbrc_file = args.file3

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
#df3['DateTime'] = pd.to_datetime(df3['Year']+'-'+df3['Month']+'-'+df3['Day']+', '+df3['Hour']+':'+df3['Minute']+':'+df3['Second'])

# Perform an outer join on date1 and date2
combined_df = pd.merge(df1, df2, left_on='DateTime', right_on='DateTime', how='outer')
# Perform an outer join on date1 and date2
combined_df = pd.merge(combined_df, df3, left_on='DateTime', right_on='DateTime', how='outer')

# Sort the combined dataframe by combodate
combined_df = combined_df.sort_values(by="DateTime")

# Write the sorted dataframe to a new CSV file
combined_df.to_csv("combined_sorted.csv", index=False)
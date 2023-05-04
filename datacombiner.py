import pandas as pd
import os
import re

heart_file = None
oxygen_file = None

for file in os.listdir("."):
    if re.search("heart", file, re.IGNORECASE):
        heart_file = file
        if oxygen_file is not None:
            break  # both files found, exit loop
    elif re.search("oxygen", file, re.IGNORECASE):
        oxygen_file = file
        if heart_file is not None:
            break  # both files found, exit loop

print("Heart rate file:", heart_file)
print("Oxygen level file:", oxygen_file)

df1=pd.read_csv(heart_file, header=1, na_values=[''], index_col=False)
df2=pd.read_csv(oxygen_file, header=1, na_values=[''], index_col=False)

# Perform an outer join on date1 and date2
combined_df = pd.merge(df1, df2, left_on='com.samsung.health.heart_rate.end_time', right_on='com.samsung.health.oxygen_saturation.end_time', how='outer')

# Create a new column called combodate by combining date1 and date2
combined_df["combodate"] = combined_df["com.samsung.health.heart_rate.end_time"].fillna(combined_df["com.samsung.health.oxygen_saturation.end_time"])

# Drop the original date1 and date2 columns
combined_df = combined_df.drop(["com.samsung.health.heart_rate.end_time", "com.samsung.health.oxygen_saturation.end_time"], axis=1)

# Sort the combined dataframe by combodate
combined_df = combined_df.sort_values(by="combodate")

# Write the sorted dataframe to a new CSV file
combined_df.to_csv("combined_sorted.csv", index=False)
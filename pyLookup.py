import pandas as pd
import numpy as np
import calendar
import time

# Excel file Name Variables, Change it as per the need
workbook_one = 'input/voice_data_message.xlsx'
workbook_two = 'input/mobile_sum.xlsx'
workbook_result = 'output/lookup_output_' + str(calendar.timegm(time.gmtime()))+ '.xlsx'

# This is the lookup field column name, this should be same in both the sheet.
lookup_key = 'Billed.POS.Number'

# This is the array of columns, which we need to fetch from the sheet, change this as per the need
# You should add the column name from the excel from where we are performing lookups
# Updated: we are fetching the column list below.
lookup_fields = []

############## START DO NOT CHANGE BELOW ################

# Pandas dataframes to hold excel file
df_first = pd.read_excel(workbook_one)
df_second = pd.read_excel(workbook_two)

# print(df_first.columns)
# print(df_second.columns.ravel())
lookup_fields = df_second.columns.ravel()
lookup_fields = lookup_fields.tolist()
lookup_fields.remove('Inventory.Status')
# print(lookup_fields)

df_temp = pd.merge(df_first, df_second[lookup_fields], on=lookup_key, how='right')
# print(df_temp)

# Drop all the rows which is present in file 2 but not in file 1
# df_temp = df_temp.drop(df_temp[df_temp['Inventory.Status'] == np.nan].index, inplace=True)
df_temp.dropna(subset=['Inventory.Status'], inplace=True)

# print(df_temp)

# Replace any NaN (if exist) to empty string
df_temp = df_temp.replace(np.nan, '', regex=True)

# Write output to output folder and file with sheet name `processed_data`
df_temp.to_excel(workbook_result, sheet_name='processed_data', index=False)

######################### END ###############################
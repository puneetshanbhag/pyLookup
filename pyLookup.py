import pandas as pd
import numpy as np
import calendar
import time

# Excel file Name Variables, Change it as per the need
workbook_one = 'input/account_number_unbilled_usage.csv'
workbook_two = 'input/MobileSum.xlsb'
workbook_result = 'output/lookup_output_' + str(calendar.timegm(time.gmtime()))+ '.xlsx'

# This is the lookup field column name, this should be same in both the sheet.
lookup_key = 'Billed.POS.Number'

# This is the array of columns, which we need to fetch from the sheet, change this as per the need
# You should add the column name from the excel from where we are performing lookups
# Updated: we are fetching the column list below.
lookup_fields = []
col_names_rawdata = ["Wireless number",
                     "Account number",
                     "User name", "Price plan description", "Peak minutes",
                     "Domestic KB", "Domestic MB", "Domestic GB", "Domestic mobile broadband connect KB",
                     "Domestic mobile broadband connect MB", "Domestic mobile broadband connect GB",
                     "International travel data kilobytes", "International travel data megabytes",
                     "International travel mobile broadband connect kilobytes",
                     "International travel mobile broadband connect megabytes", "Domestic TXT received",
                     "Domestic TXT sent", "International (while in U.S.) TXT received",
                     "International (while in U.S.) TXT sent", "International travel (Outside U.S.) TXT received",
                     "International travel (Outside U.S.) TXT sent", "PIX/FLIX received", "PIX/FLIX sent"]

############## START DO NOT CHANGE BELOW ################

def format_key(val):
    """
    format the lookup_key string value to a int64 from csv
     - Remove "-"
    """
    if val == '':
        return np.nan
    new_val = val.replace(r'\D', '')
    return np.int64(new_val)

# Pandas dataframes to hold excel file
df_first = pd.read_csv(workbook_one, skiprows=18, usecols=col_names_rawdata)

# Copy 'Wireless number' to 'Billed.POS.Number' for lookup
df_first.insert(0, lookup_key, df_first['Wireless number'].str.replace(r'\D', ''))

# Replace hypen in Wireless number example : 220-111-1111 will be replace to 2201111111
df_first[lookup_key] = df_first[lookup_key].apply(format_key)

# print(df_first)

df_second = pd.read_excel(workbook_two)

# Move 'Billed.POS.Number' column to first position in the sheet
first_column = df_second.pop(lookup_key)
df_second.insert(0, lookup_key, first_column)

# print('######################')
# print(df_second)

# Fetching the columns from second sheet and converting it to a list object and cleaningup
# print(df_first.columns)
# print(df_second.columns.ravel())
lookup_fields = df_second.columns.ravel()
lookup_fields = lookup_fields.tolist()

# print(df_first.dtypes)
# print('######################')
# print(df_second.dtypes)

df_temp = pd.merge(df_first, df_second[lookup_fields], on=lookup_key, how='right')
# print(df_temp)

# Drop all the rows which is present in file 2 but not in file 1
df_temp.dropna(subset=['Wireless number'], inplace=True)

# print(df_temp)

# Replace any NaN (if exist) to empty string
df_temp = df_temp.replace(np.nan, '', regex=True)

# Write output to output folder and file with sheet name `processed_data`, change this if required
df_temp.to_excel(workbook_result, sheet_name='processed_data', index=False)

######################### END ###############################
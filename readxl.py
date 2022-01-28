######### THIS IS A SAMPLE CODE NOT USED IN THE MAIN SCRIPT YOU CAN IGNORE THIS #########

import pandas as pd
import numpy as np

workbook_rawdata = 'input/account_number_unbilled_usage.csv'

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

df_rawdata = pd.read_csv(workbook_rawdata, skiprows=18, usecols=col_names_rawdata)

df_rawdata.rename(columns={'Wireless number': 'Billed.POS.Number'}, inplace=True)
df_rawdata['Billed.POS.Number'] = df_rawdata['Billed.POS.Number'].str.replace(r'\D', '')


print(df_rawdata)

df_rawdata.rename(columns={'Billed.POS.Number': 'Wireless number'}, inplace=True)
df_rawdata.to_excel("output/test.xlsx")

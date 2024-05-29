# install the comtradeapicall first:
# py -m pip install comtradeapicall
# py -m pip install --upgrade comtradeapicall
# may need to install other dependencies
from datetime import timedelta
from datetime import date
import comtradeapicall

import pandas as pd
import requests
import comtradeapicall
# set some variables
subscription_key = '<YOUR KEY>' # comtrade api subscription key (from comtradedeveloper.un.org), some preview and metadata/reference API calls do not require key
#For Example
# subscription_key = '3e7fddeb49ed49aab3b139cb90ceb1fc' # comtrade api subscription key (from comtradedeveloper.un.org)

# set some variables again
today = date.today()
yesterday = today - timedelta(days=1)
lastweek = today - timedelta(days=7)


#Call API to collect data in mydf
mydf = comtradeapicall.getFinalData(subscription_key, typeCode='C', freqCode='A', clCode='HS', period='2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023',
                                    reporterCode=None, cmdCode='8534,8541,854110,854121,854129,854130,854140,854150,854160,854190,8542,854231,854232,854233,854239,854290,854141,854142,854143,854149,854151,854159', flowCode='M,X',
                                    partnerCode='0', partner2Code='0', customsCode='C00', motCode='0', format_output='JSON',
                                    aggregateBy=None, breakdownMode='classic', countOnly=None, includeDesc=True)

#Select Feature
new = mydf[['period', 'reporterISO', 'reporterDesc', 'flowDesc', 'cmdCode', 'cmdDesc', 'primaryValue']]
new.rename(columns={'period': 'Year','reporterISO': 'CountryISO', 'flowDesc': 'FlowDesc', 'reporterDesc': 'Country1', 'cmdCode': 'CmdCode', 'cmdDesc': 'CmdDesc', 'primaryValue':'PrimaryValue'}, inplace=True)

#**Create Total Import-Export by year
# Filter DataFrame for imports
imports = new[new['FlowDesc'] == 'Import']
# Filter DataFrame for exports
exports = new[new['FlowDesc'] == 'Export']
# Group the filtered DataFrames by 'Year' and calculate the sum of 'PrimaryValue' for each year
imports_yearly_total = imports.groupby('Year')['PrimaryValue'].sum()
exports_yearly_total = exports.groupby('Year')['PrimaryValue'].sum()
# Create new DataFrames to store the total import and export values for each year
imports_yearly_total_df = imports_yearly_total.reset_index()
exports_yearly_total_df = exports_yearly_total.reset_index()
# # Rename columns to differentiate between import and export
imports_yearly_total_df.rename(columns={'PrimaryValue': 'GlobalImport'}, inplace=True)
exports_yearly_total_df.rename(columns={'PrimaryValue': 'GlobalExport'}, inplace=True)
# Merge the import and export DataFrames on 'Year'
imex_yearly_total = pd.merge(imports_yearly_total_df, exports_yearly_total_df, on='Year', how='outer')

#**Create Percentage Table for Viz
per = new.groupby(['Year', 'Country1', 'FlowDesc']).agg({'PrimaryValue': 'sum'}).reset_index()
per.rename(columns={'PrimaryValue': 'Value', 'Country1': 'Country2'}, inplace=True)

#**Save Data in CSV
new.to_csv('UNTradeforVis.csv', index=False, encoding='utf-8-sig')
imex_yearly_total.to_csv('GlobalUNTrade.csv', index=False, encoding='utf-8-sig')
per.to_csv('perbycountry.csv', index=False, encoding='utf-8-sig')
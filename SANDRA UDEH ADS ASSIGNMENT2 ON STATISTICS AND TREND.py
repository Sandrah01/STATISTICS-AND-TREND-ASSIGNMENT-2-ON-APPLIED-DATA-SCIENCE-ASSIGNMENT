# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 12:08:35 2022

@author: udehs
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def extract_data(world_climate,countries,columns,indicator):
    '''
  This function manipulate the world bank climate data using pandas dataframes
  Args:
      filename(str): The name of the file to read the data from.
      countries: preferred choice of country to be read.
      columns: the columns to be returned.
      indicator: choice of dataset to work with.
  Returns:
      dataframe[pandas.core.frame.DataFrame]: A dataframe containing the worldbank data.
   '''
   
    # Reading the data from the file
    df = pd.read_csv(world_climate, skiprows=3) 
    
    # This makes column indicator name equivalent to indicator
    df = df[df['Indicator Name'] == indicator]

    # Makes the first row as the header
    df = df[columns]
    df.set_index('Country Name', inplace = True)
    df = df.loc[countries] # The loc keyword produce the location of desired column
    return df,df.transpose() # The preprocessed and transposed data are returned respectively


# Parameters to extract and manipulate the data 
world_climate = 'API_19_DS2_en_csv_v2_4700503.csv'  # The worldbank csv file
countries = ['Canada','Japan','Zambia','Albania','Vietnam']
columns = ['Country Name', '2000','2002','2004','2006','2008','2010', '2012','2014']
indicators = ['Electric power consumption (kWh per capita)', 'Population growth (annual %)', 'CO2 emissions (metric tons per capita)', 'Cereal yield (kg per hectare)','Forest area (% of land area)', 'Arable land (% of land area)']

# This returns the transposed data for electric power consumption
df_epc_country, df_epc_year = extract_data(world_climate,countries,columns,indicators[0])


# Parameters to extract and manipulate the data 
world_climate = 'API_19_DS2_en_csv_v2_4700503.csv'  # The worldbank csv file
countries = ['Canada','Japan','Zambia','Albania','Vietnam']
columns = ['Country Name', '2000','2002','2004','2006','2008','2010', '2012','2014']
indicators = ['Electric power consumption (kWh per capita)', 'Population growth (annual %)', 'CO2 emissions (metric tons per capita)', 'Cereal yield (kg per hectare)','Forest area (% of land area)', 'Arable land (% of land area)']

# This returns the function (extract_data) with Electric power consumption (kWh per capita) indicator
df_epc_country, df_epc_year = extract_data(world_climate,countries,columns,indicators[0])

# This returns the function (extract_data) Population growth (annual %)indicator
df_pop_country, df_pop_year = extract_data(world_climate,countries,columns,indicators[1])

# This returns the function (extract_data) with CO2 emissions (metric tons per capita) indicator
df_co2_country, df_co2_year = extract_data(world_climate,countries,columns,indicators[2])

# This returns the function (extract_data) with Cereal yield (kg per hectare) indicator
df_cereal_country, df_cereal_year = extract_data(world_climate,countries,columns,indicators[3])

# This returns the function (extract_data) with Forest area (% of land area) indicator
df_forest_country, df_forest_year = extract_data(world_climate,countries,columns,indicators[4])

#  This returns the function (extract_data) with Arable land (% of land area) indicator
df_arable_country, df_arable_year = extract_data(world_climate,countries,columns,indicators[5])



#returns column in electricity power consumption as country
print(df_epc_country)
















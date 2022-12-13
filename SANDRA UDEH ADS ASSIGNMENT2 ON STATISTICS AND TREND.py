# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 12:08:35 2022

@author: udehs
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def extract_data(world_climate, countries, columns, indicator):
    
    '''
  This function manipulate the world bank climate data using pandas dataframes
  Args:
      world_climate(str): The name of the file to read the data from.
      countries: preferred choice of country to be read.
      fcolumns: the columns to be returned.
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
    # The loc keyword produce the location of desired column
    df = df.loc[countries] 
    # The preprocessed and transposed data are returned respectively
    return df, df.transpose() 


# Parameters to extract and manipulate the data 
world_climate = 'API_19_DS2_en_csv_v2_4700503.csv'  
countries = ['Canada','Japan','Zambia','Albania','Vietnam']
columns = ['Country Name', '2000','2002','2004','2006','2008','2010', '2012','2014']
indicators = ['Electric power consumption (kWh per capita)', 'Population growth (annual %)', 'CO2 emissions (metric tons per capita)', 'Arable land (% of land area)']



# This returns the function (extract_data) with Electric power consumption (kWh per capita) indicator
df_epc_country, df_epc_year = extract_data(world_climate, countries, columns, indicators[0])

# This returns the function (extract_data) Population growth (annual %)indicator
df_pop_country, df_pop_year = extract_data(world_climate, countries, columns, indicators[1])

# This returns the function (extract_data) with CO2 emissions (metric tons per capita) indicator
df_co2_country, df_co2_year = extract_data(world_climate, countries, columns, indicators[2])

# This returns the function (extract_data) with Arable land (% of land area) indicator
df_arable_country, df_arable_year = extract_data(world_climate, countries, columns, indicators[3])



#returns column in electricity power consumption as country
print(df_epc_country)

#returns column in electric power consumption as year
print(df_epc_year)

#returns colunmn in population as country
print(df_pop_country)

#returns colunmn in population as year
print(df_pop_year)

#returns colunmn in co2 as country
print(df_co2_country)

#returns colunmn in population as year
print(df_co2_year)

#returns colunmn in population as country
print(df_arable_country)

#returns colunmn in population as year
print(df_arable_year)



# statistical property to describe the population data
print(df_pop_country.describe())

# statistical property to describe the co2 data
print(df_co2_country.describe())



def multiple_line_plot(x_data, y_data, xlabel, ylabel, title, labels, colors):
    '''
   
    This function defines multiple line plot, below are the attributes
    x_data: this uses years of the indicator to state the index
    y_data: this uses country of the indicator
    xlabel: label for x-axis
    ylabel: label for y-axis
    title:  shows the title of the plot
    labels: these are the labels of each line plot y the legend function
    colors: the colours for each representation
    
    '''
    plt.figure(figsize=(12,8))
    plt.title(title, fontsize=20)
    
    # This produces choice of plot by looping over the dataframe
    for i in range(len(y_data)): 
        plt.plot(x_data, y_data[i], label=labels[i], color=colors[i])
    plt.xlabel(xlabel, fontsize=25)
    plt.ylabel(ylabel, fontsize=25)
    plt.rcParams["figure.dpi"] = 1000
    plt.legend(bbox_to_anchor=(1,1))
    plt.show()
    return


# parameters for plotting multiple line plot of Electric power consumption (kWh per capita)
x_data = df_epc_year.index # This returns the row index as the value of x axis 
y_data = [df_epc_year['Canada'],
          df_epc_year['Japan'],
          df_epc_year['Zambia'],
          df_epc_year['Albania'],
          df_epc_year['Vietnam']]
xlabel = 'years'
ylabel = 'Electric power consumption'
labels = ['Canada','Japan','Zambia','Albania','Vietnam']
colors = ['blue', 'red', 'black', 'green', 'purple']
title = 'Electric power consumption (kWh per capita) for 5 countries'

# The above attribute are passed into the function to give desired plot
multiple_line_plot(x_data, y_data, xlabel, ylabel, title, labels, colors)


# parameters for plotting multiple line plot of polulation growth (% annual)
x_data = df_pop_year.index  
y_data = [df_pop_year['Canada'],
          df_pop_year['Japan'],
          df_pop_year['Zambia'],
          df_pop_year['Albania'],
          df_pop_year['Vietnam']]
xlabel = 'years'
ylabel = 'population growth'
labels = ['Canada','Japan','Zambia','Albania','Vietnam']
colors = ['blue', 'red', 'black', 'green', 'purple']
title = 'polulation growth (% annual) for 5 countries'

# The above attribute are passed into the function to give desired plot
multiple_line_plot(x_data, y_data, xlabel, ylabel, title, labels, colors)



def Grouped_barplot(data, title):
    
    """
    Plots grouped bar charts.
    
    Args:
        Data: The data to plot.
        title: The title of the plot.
        
    Returns:
        None
        
    """
    # Set the title of the plot
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.rcParams["figure.dpi"] = 1000
    plt.legend(bbox_to_anchor=(1,1))
    plt.show()


# parameters for plotting grouped barplot for Co2 emission
Data = df_co2_country
Data.plot(kind='bar')
xlabel = 'countries'
ylabel = 'Co2 emission'
# The above attribute are passed into the function to give desired plo
Grouped_barplot(Data, 'Grouped barplot for  Co2 emission')


#parameters for plotting grouped barplot for arable land
Data = df_arable_country
Data.plot(kind='bar')
xlabel = 'countries'
ylabel = 'Arable land'
# The above attribute are passed into the function to give desired plot
Grouped_barplot(Data, 'Grouped barplot for arable land')


# we create a dataframe for canada which takes 4 indicators as parameter
Data_Canada = pd.DataFrame(
{'Electric power consumption(kWh per capita)': df_epc_year['Canada'],
'Population growth(annual %)': df_pop_year['Canada'],
'CO2 emissions(metric tons per capita)': df_co2_year['Canada'],
 'Arable land (% of land area)':df_arable_year['Canada']},
['2000','2002','2004','2006','2008','2010', '2012','2014'])

# Calculate the correlation matrix for Canada
print(Data_Canada.corr())

def heatmap_Canada(Data_Canada, size=6):
    
    """
    function creates heatmap of correlation matrix for each pair of columns in the dataframe for Canada against the indicators selected

Input:
     Data_Canada: Transposed Dataframe for Canada
     size: vertical and horizontal size of the plot (inch)

   """
corr = Data_Canada.corr()
fig, ax = plt.subplots(figsize=(8,5))
ax.matshow(corr, cmap='Blues') 

#setting ticks to column names
plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
plt.yticks(range(len(corr.columns)), corr.columns)
plt.title('Heatmap for Canada')
plt.show




# we create a dataframe for Albania which takes 4 indicators as parameter
Data_Albania = pd.DataFrame(
{'Electric power consumption': df_epc_year['Albania'],
'Population growth': df_pop_year['Albania'],
'CO2 emissions': df_co2_year['Albania'],
'Arable land ':df_arable_year['Albania']},
['2000','2002','2004','2006','2008','2010', '2012','2014'])

# Calculate the correlation matrix for Albania
print(Data_Albania.corr())

def heatmap_Albania(Data_Albania, size=6):
    """
    function creates heatmap of correlation matrix for each pair of columns in the dataframe for Albania against the indicators selected

Input:
     Data_Albania: Transposed Dataframe for Albania
     size: vertical and horizontal size of the plot (inch)

   """
corr = Data_Albania.corr()
fig, ax = plt.subplots(figsize=(8,5))
ax.matshow(corr, cmap='Purples')
   
#setting ticks to column names
plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
plt.yticks(range(len(corr.columns)), corr.columns)
plt.title(' Heatmap for Albania')
plt.show














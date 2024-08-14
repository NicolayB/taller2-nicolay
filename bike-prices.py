import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("BikePrices.csv")
df.head()

df.shape

df["Brand"].unique()

df.groupby("Brand").count()

df["Brand"].value_counts()

df.describe()

# Porcentaje de motos marca Honda
count = df["Brand"].value_counts()
perc_honda = (count.loc["Honda"]/count.sum())*100
print(f"Honda Rate = {perc_honda:.2f}%")

# Número de duplicados
duplicates = len(df[df.duplicated()])
print(f'Number of Duplicate Entries: {duplicates}')

# Número de valores perdidos
missing_values = df.isnull().sum().sum()
print(f'Number of Missing Values: {missing_values}')

# Tipos de datos en el dataset
types = df.dtypes.value_counts()
print('Number of Features: %d'%(df.shape[1]))
print('Number of Bikes: %d'%(df.shape[0]))
print('Data Types and Frequency in Dataset:')
print(types)

hist_pd = df.hist("Selling_Price")
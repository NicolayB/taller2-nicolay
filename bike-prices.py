import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf
from scipy.optimize import brentq
from scipy import stats

df = pd.read_csv("BikePrices.csv")
print(df.head())
print("\n", df.shape)

print("\n", df["Brand"].unique())

print("\n", df.groupby("Brand").count())

print("\n", df["Brand"].value_counts())

print("\n", df.describe())

# Porcentaje de motos marca Honda
count = df["Brand"].value_counts()
perc_honda = (count.loc["Honda"]/count.sum())*100
print("\n", f"Honda Rate = {perc_honda:.2f}%")

# Número de duplicados
duplicates = len(df[df.duplicated()])
print("\n", f'Number of Duplicate Entries: {duplicates}')

# Número de valores perdidos
missing_values = df.isnull().sum().sum()
print("\n", f'Number of Missing Values: {missing_values}')

print("\n")

# Tipos de datos en el dataset
types = df.dtypes.value_counts()
print('Number of Features: %d'%(df.shape[1]))
print('Number of Bikes: %d'%(df.shape[0]))
print('Data Types and Frequency in Dataset:')
print(types)

# Promedio de preciosa de venta
media = round(np.mean(df["Selling_Price"]),2)
print(media)

#Estadisticas descriptivas del precio de venta
mediana = round(np.std(df["Selling_Price"]),2)
varianza = round(np.var(df["Selling_Price"]),2)
rango = np.ptp(df["Selling_Price"])
print(rango)




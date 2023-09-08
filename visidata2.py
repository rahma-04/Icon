import streamlit as st
import pandas as pd
# import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from mpl_toolkits.mplot3d import Axes3D

# Load the data
data = pd.read_excel('aduan_pelanggan_icon.xlsx')

# Title and subheader
st.title('Analisis 2')
st.subheader('Data Aduan Pelanggan Terhadap Bulan dan Tahun')

# Display the data
# st.write(data)

# Pre-processing

# Drop unused columns
df = data.drop(
    ['VIP', 'Pending Reason',
     'SLA', 'Resolved On Agent',
     'Resolved By Agent'], axis=1)

# Drop rows with null values in 'Resolved On' column
df.dropna(subset=['ResolvedOn'], inplace=True)

# Rename columns
df.rename(columns={'Incident No': 'IncidentNo',
                   'Assign On': 'AssignOn',
                   'Created On': 'CreatedOn',
                   'Created By': 'CreatedBy',
                   'Resolved On': 'ResolvedOn'}, inplace=True)

# Display the processed data if needed
# st.subheader('Processed Data')


# Barplot jumlah aduan per tahun
df_createOn = df['CreatedOn'].dt.year
jumCreate = df_createOn.value_counts().sort_index()
plt.figure(figsize=(8, 5))
jumCreate.plot(kind='bar', color='skyblue')
plt.title('Jumlah Aduan Aplikasi Icon Plus per Tahun')
plt.xlabel('Tahun Aduan')
plt.ylabel('Jumlah Aduan')
plt.xticks(rotation=0)
plt.grid(True)
st.pyplot(plt)

# Stacked bar plot 2020
df_yCreateOn = df['CreatedOn'].dt.year
df_mCreateOn = df['CreatedOn'].dt.month
df_2020 = df[df_yCreateOn == 2020]
grouped_data = df_2020.groupby([df_mCreateOn, 'service']).size().unstack().fillna(0)
plt.figure(figsize=(17, 13))
grouped_data.plot(kind='bar', stacked=True)
plt.title('Jumlah Aduan Aplikasi Icon Plus per Bulan Tahun 2020')
plt.xlabel('Bulan')
plt.ylabel('Jumlah Aduan')
plt.xticks(rotation=0)
plt.legend(title='Aplikasi')
plt.grid(True)
st.pyplot(plt)

# Stacked bar plot 2021
df_yCreateOn = df['CreatedOn'].dt.year
df_mCreateOn = df['CreatedOn'].dt.month
df_2021 = df[df_yCreateOn == 2021]
grouped_data = df_2021.groupby([df_mCreateOn, 'service']).size().unstack().fillna(0)
plt.figure(figsize=(17, 13))
grouped_data.plot(kind='bar', stacked=True)
plt.title('Jumlah Aduan Aplikasi Icon Plus per Bulan Tahun 2021')
plt.xlabel('Bulan')
plt.ylabel('Jumlah Aduan')
plt.xticks(rotation=0)
plt.legend(title='Aplikasi')
plt.grid(True)
st.pyplot(plt)

# Stacked bar plot 2022
df_yCreateOn = df['CreatedOn'].dt.year
df_mCreateOn = df['CreatedOn'].dt.month
df_2022 = df[df_yCreateOn == 2022]
grouped_data = df_2022.groupby([df_mCreateOn, 'service']).size().unstack().fillna(0)
plt.figure(figsize=(17, 13))
grouped_data.plot(kind='bar', stacked=True)
plt.title('Jumlah Aduan Aplikasi Icon Plus per Bulan Tahun 2022')
plt.xlabel('Bulan')
plt.ylabel('Jumlah Aduan')
plt.xticks(rotation=0)
plt.legend(title='Aplikasi')
plt.grid(True)
st.pyplot(plt)

# Stacked bar plot 2023
df_yCreateOn = df['CreatedOn'].dt.year
df_mCreateOn = df['CreatedOn'].dt.month
df_2023 = df[df_yCreateOn == 2023]
grouped_data = df_2023.groupby([df_mCreateOn, 'service']).size().unstack().fillna(0)
plt.figure(figsize=(17, 13))
grouped_data.plot(kind='bar', stacked=True)
plt.title('Jumlah Aduan Aplikasi Icon Plus per Bulan Tahun 2023')
plt.xlabel('Bulan')
plt.ylabel('Jumlah Aduan')
plt.xticks(rotation=0)
plt.legend(title='Aplikasi', loc='upper left')
plt.grid(True)
st.pyplot(plt)
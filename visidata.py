import streamlit as st
import pandas as pd
# import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Load the data
data = pd.read_excel('aduan_pelanggan_icon.xlsx')

# Title and subheader
st.title('Analisis 1')
st.subheader('Layanan Aplikasi terhadap Kategori Aduan')
st.subheader('Data Aduan Pelanggan')

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
st.write(df)

# Create bar plots

# Bar plot for 'service'
st.subheader('Jumlah Aduan Berdasarkan Jenis Layanan Aplikasi')
plt.figure(figsize=(10, 6))
total_service = df['service'].value_counts()
sort = total_service.sort_values(ascending=True)
bars = plt.barh(sort.index, sort.values)
plt.xlabel('Jumlah Aduan')
plt.ylabel('Jenis Aplikasi')
for bar in bars:
    width = bar.get_width()
    plt.text(width, bar.get_y() + bar.get_height() / 2, f'{int(width)}', ha='left', va='center')
st.pyplot(plt)

# Bar plot for 'Category' based on 'service'
# st.subheader('Category Bar Plots')
top3_service = total_service
df_top3service = df[df['service'].isin(top3_service.index)]

st.subheader('Jumlah Aduan Berdasarkan Kategori Dari Layanan Aplikasi')

selected_service = st.selectbox('Pilih Layanan Aplikasi', top3_service.index)

# Filter the DataFrame based on the selected service
df_selected_service = df[df['service'] == selected_service]

# Create a bar plot for the selected service category
st.subheader(f'Aplikasi {selected_service}')
jumlah = df_selected_service['Category'].value_counts()
plt.figure(figsize=(10, 6))
sort = jumlah.sort_values(ascending=True)
bars = plt.barh(sort.index, sort.values)
plt.xlabel(f'Jumlah Aduan {selected_service}')
plt.ylabel(f'Kategori {selected_service}')
for bar in bars:
    width = bar.get_width()
    plt.text(width, bar.get_y() + bar.get_height() / 2, f'{int(width)}', ha='left', va='center')
st.pyplot(plt)





# # Plot for 'AirCRM'
# st.subheader('Aplikasi AirCRM')
# df_AirCRM = df_top3service.loc[df_top3service['service'] == 'AirCRM']
# jumlah2 = df_AirCRM['Category'].value_counts()
# plt.figure(figsize=(10, 6))
# sort = jumlah2.sort_values(ascending=True)
# bars = plt.barh(sort.index, sort.values)
# plt.xlabel('Jumlah Aduan AirCRM')
# plt.ylabel('Kategori AirCRM')
# for bar in bars:
#     width = bar.get_width()
#     plt.text(width, bar.get_y() + bar.get_height() / 2, f'{int(width)}', ha='left', va='center')
# st.pyplot(plt)

# # Plot for 'iOffice Internal'
# st.subheader('Aplikasi iOffice Internal')
# df_iOfficeInt = df_top3service.loc[df_top3service['service'] == 'iOffice Internal']
# jumlah1 = df_iOfficeInt['Category'].value_counts()
# plt.figure(figsize=(10, 6))
# sort = jumlah1.sort_values(ascending=True)
# bars = plt.barh(sort.index, sort.values)
# plt.xlabel('Jumlah Aduan iOffice Internal')
# plt.ylabel('Kategori iOffice Internal')
# for bar in bars:
#     width = bar.get_width()
#     plt.text(width, bar.get_y() + bar.get_height() / 2, f'{int(width)}', ha='left', va='center')
# st.pyplot(plt)

# # Plot for 'AirLis'
# st.subheader('Aplikasi AirLis')
# df_AirLis = df_top3service.loc[df_top3service['service'] == 'AirLis']
# jumlah3 = df_AirLis['Category'].value_counts()
# plt.figure(figsize=(10, 6))
# sort = jumlah3.sort_values(ascending=True)
# bars = plt.barh(sort.index, sort.values)
# plt.xlabel('Jumlah Aduan iOffice Internal')
# plt.ylabel('Kategori iOffice Internal')
# for bar in bars:
#     width = bar.get_width()
#     plt.text(width, bar.get_y() + bar.get_height() / 2, f'{int(width)}', ha='left', va='center')
# st.pyplot(plt)

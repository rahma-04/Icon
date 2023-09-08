import streamlit as st
import pandas as pd
# import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Load the data
data = pd.read_excel('aduan_pelanggan_icon.xlsx')

# Title and subheader
st.title('Analisis 3 ')
st.subheader('Data Platform Aduan Terhadap Waktu')

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


# Jumlah status aduan
st.subheader('Pie Chart Jumlah Aduan Berdasarkan Sumber')
df_source = df['Source'].value_counts()
fig = px.pie(df_source, names=df_source.index, values=df_source.values)
st.plotly_chart(fig)

# Email per waktu
df_email = df[df['Source'] == 'Email']
def label_waktu(jam):
    if 6 <= jam < 12:
        return 'Pagi'
    elif 12 <= jam < 18:
        return 'Siang'
    elif 18 <= jam < 24:
        return 'Sore'
    else:
        return 'Malam'

email = df_email['CreatedOn'].dt.hour.apply(label_waktu)
emailperHour = email.value_counts()
emailperHour = emailperHour.reindex(['Pagi', 'Siang', 'Sore', 'Malam'])

# Self service per waktu
df_sService = df[df['Source'] == 'Self Service']
def label_waktu(jam):
    if 6 <= jam < 10.59:
        return 'Pagi'
    elif 11 <= jam < 14.59:
        return 'Siang'
    elif 15 <= jam < 18.59:
        return 'Sore'
    elif 19 <= jam < 22.59:
        return 'Malam'
    else:
        return 'Dini Hari'

selfService = df_sService['CreatedOn'].dt.hour.apply(label_waktu)
selfServiceperHour = selfService.value_counts()
selfServiceperHour = selfServiceperHour.reindex(['Pagi', 'Siang', 'Sore', 'Malam', 'Dini Hari'])

# Telepon terhadap waktu
df_phone = df[df['Source'] == 'Phone']
phone = df_phone['CreatedOn'].dt.hour.apply(label_waktu)
phoneperHour = phone.value_counts()
phoneperHour = phoneperHour.reindex(['Pagi', 'Siang', 'Sore', 'Malam', 'Dini Hari'])

# Define a color palette to match the pie chart colors
color_palette = ['blue', 'lightblue', 'red']

# Create a line chart for all three sources with matching colors
st.subheader('Jumlah Aduan Berdasarkan Jenis Layanan Aplikasi')
plt.figure(figsize=(10, 6))
plt.plot(emailperHour.index, emailperHour.values, label='Email', marker='o', color=color_palette[0])
plt.plot(selfServiceperHour.index, selfServiceperHour.values, label='Self Service', marker='o', color=color_palette[1])
plt.plot(phoneperHour.index, phoneperHour.values, label='Phone', marker='o', color=color_palette[2])
plt.xlabel('Label Waktu')
plt.ylabel('Jumlah Aduan')
plt.title('Jumlah Aduan Berdasarkan Jenis Layanan Aplikasi per Waktu')
plt.legend()
plt.grid(True)
st.pyplot(plt)
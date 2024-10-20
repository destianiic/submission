import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
hour_df = pd.read_csv("hour.csv")
day_df = pd.read_csv("day.csv")

# Convert 'dteday' to datetime format
day_df['dteday'] = pd.to_datetime(day_df['dteday'])

# Set title of the dashboard
st.title("Bike Rentals Analysis Dashboard")

# Section for exploring the factors affecting bike rentals
st.header("Factors Affecting Bike Rentals")

# Bar Chart: Rentals by Season
st.subheader("Bike Rentals by Season")
season_counts = day_df['season'].value_counts()
season_labels = ['Winter', 'Spring', 'Summer', 'Fall']
plt.figure(figsize=(8, 6))
plt.bar(season_labels, season_counts)
plt.title('Bike Rentals by Season')
plt.xlabel('Season')
plt.ylabel('Number of Rentals')
st.pyplot(plt)

# Pie Chart: Rentals on Working Days vs. Non-Working Days
st.subheader("Rentals on Working Days vs. Non-Working Days")
workingday_counts = day_df['workingday'].value_counts()
workingday_labels = ['Non-Working Day', 'Working Day']
plt.figure(figsize=(8, 6))
plt.pie(workingday_counts, labels=workingday_labels, autopct='%1.1f%%', startangle=90)
plt.title('Rentals on Working Days vs. Non-Working Days')
st.pyplot(plt)

# Histogram: Rentals vs. Humidity
st.subheader("Bike Rentals vs. Humidity")
plt.figure(figsize=(10, 6))
plt.hist(day_df['hum'], bins=20, color='g')
plt.title('Bike Rentals vs. Humidity')
plt.xlabel('Humidity')
plt.ylabel('Frequency of Rentals')
st.pyplot(plt)

# Bar Chart: Rentals vs. Temperature
st.subheader("Average Bike Rentals per Temperature Group")
temp_bins = pd.cut(day_df['temp'], bins=10)  # Group temperatures into 10 bins
temp_rentals = day_df.groupby(temp_bins)['cnt'].mean()  # Calculate average rentals per bin
plt.figure(figsize=(10, 6))
temp_rentals.plot(kind='bar', color='b')
plt.title('Average Bike Rentals per Temperature Group')
plt.xlabel('Temperature (Binned)')
plt.ylabel('Average Number of Rentals')
st.pyplot(plt)

# Advanced Analysis Section
st.header("Advanced Analysis")

# Geoanalysis based on season (season as a proxy for different regions)
st.subheader("Total Bike Rentals by Season")
season_rentals = day_df.groupby('season')['cnt'].sum()
plt.figure(figsize=(10, 6))
season_rentals.plot(kind='bar', color='c')
plt.title('Total Bike Rentals by Season')
plt.xlabel('Season')
plt.ylabel('Total Rentals')
st.pyplot(plt)

# Manual grouping of bike rentals by season
st.subheader('Average Bike Rentals per Season')
season_groups = day_df.groupby('season')['cnt'].mean()
plt.figure(figsize=(10, 6))
season_groups.plot(kind='bar', color='m')
plt.title('Average Bike Rentals per Season')
plt.xlabel('Season')
plt.ylabel('Average Rentals')
st.pyplot(plt)

# RFM Analysis Section
st.header('RFM Analysis')

# Add 'Recency' as days since last entry
latest_date = day_df['dteday'].max()
day_df['Recency'] = (latest_date - day_df['dteday']).dt.days

# Calculate Frequency (total rentals per day of the week)
rental_frequency = day_df.groupby('weekday')['cnt'].sum()

# Monetary value: Total rentals per day
monetary_value = day_df.groupby('dteday')['cnt'].sum()

# Display RFM
rfm_df = pd.DataFrame({
    'Recency': day_df.groupby('dteday')['Recency'].mean(),
    'Frequency': rental_frequency,
    'Monetary': monetary_value
})

st.write(rfm_df.head())

# Conclusions Section
st.header("Conclusions")
st.write("""
1. Terdapat beberapa faktor yang mempengaruhi jumlah rental sepeda, seperti:
    - season (rental sepeda semakin banyak saat season 3)
    - working days dimana jumlah rental akan semakin tinggi pada working day dibandingkan weekend
    - kondisi cuaca dimana semakin tinggi temperatur maka rental akan tinggi, sebaliknya jika kelembapan dan kecepatan semakin tinggi maka rental akan berkurang
2. Temperatur memiliki peranan tinggi terhadap jumlah rental sepeda, dimana:
    - semakin tinggi temperatur maka rental sepeda akan semakin banyak juga
    - semakin tinggi kelembapan dan kecepatan angin akan membuat rental sepeda semakin kecil/rendah
""")

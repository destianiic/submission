import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the datasets using the full paths
hour_df = pd.read_csv("hour.csv")
day_df = pd.read_csv("day.csv")

# Convert 'dteday' to datetime format
day_df['dteday'] = pd.to_datetime(day_df['dteday'])

# Set title of the dashboard
st.title("Bike Rentals Analysis Dashboard")

# Section for exploring the factors affecting bike rentals
st.header("Factors Affecting Bike Rentals")

# Visualization: Rentals by Season
st.subheader("Bike Rentals by Season")
plt.figure(figsize=(10, 6))
sns.boxplot(x='season', y='cnt', data=day_df)
plt.title('Bike Rentals by Season')
st.pyplot(plt)

# Visualization: Rentals on Holidays vs. Non-Holidays
st.subheader("Rentals on Holidays vs. Non-Holidays")
plt.figure(figsize=(10, 6))
sns.boxplot(x='holiday', y='cnt', data=day_df)
plt.title('Bike Rentals on Holidays vs. Non-Holidays')
st.pyplot(plt)

# Visualization: Rentals on Working Days vs. Non-Working Days
st.subheader("Rentals on Working Days vs. Non-Working Days")
plt.figure(figsize=(10, 6))
sns.boxplot(x='workingday', y='cnt', data=day_df)
plt.title('Bike Rentals on Working Days vs. Non-Working Days')
st.pyplot(plt)

# Section for exploring the impact of weather conditions
st.header("Impact of Weather Conditions on Bike Rentals")

# Visualization: Rentals vs. Temperature
st.subheader("Bike Rentals vs. Temperature")
plt.figure(figsize=(10, 6))
sns.scatterplot(x='temp', y='cnt', data=day_df)
plt.title('Bike Rentals vs. Temperature')
st.pyplot(plt)

# Visualization: Rentals vs. Humidity
st.subheader("Bike Rentals vs. Humidity")
plt.figure(figsize=(10, 6))
sns.scatterplot(x='hum', y='cnt', data=day_df)
plt.title('Bike Rentals vs. Humidity')
st.pyplot(plt)

# Visualization: Rentals vs. Windspeed
st.subheader("Bike Rentals vs. Windspeed")
plt.figure(figsize=(10, 6))
sns.scatterplot(x='windspeed', y='cnt', data=day_df)
plt.title('Bike Rentals vs. Windspeed')
st.pyplot(plt)

# Visualization: Correlation Heatmap
st.subheader("Correlation Between Weather Conditions and Rentals")
plt.figure(figsize=(10, 6))
sns.heatmap(day_df[['temp', 'hum', 'windspeed', 'cnt']].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Between Weather Conditions and Rentals')
st.pyplot(plt)

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

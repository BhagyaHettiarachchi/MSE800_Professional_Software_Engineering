import pandas as pd
import matplotlib.pyplot as plt

# Define the data
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

auckland_temps = [20.0, 20.3, 18.5, 15.8, 13.3, 11.1, 10.5, 11.3, 13.8, 15.5, 17.5, 19.0]
christchurch_temps = [21.1, 20.0, 17.5, 13.5, 10.0, 7.5, 6.0, 7.5, 9.5, 11.5, 14.0, 16.5]

# Create a DataFrame
df = pd.DataFrame({
    'Month': months,
    'Auckland': auckland_temps,
    'Christchurch': christchurch_temps
})

# Plot the data
plt.figure(figsize=(12, 6))
plt.plot(df['Month'], df['Auckland'], marker='o', label='Auckland')
plt.plot(df['Month'], df['Christchurch'], marker='s', label='Christchurch')

plt.title('Average Monthly Temperatures: Auckland vs Christchurch')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

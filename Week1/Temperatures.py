import numpy as np

temperatures = np.array([18.5, 19, 20, 25.0, 2, 30, 13.9])
days_of_week = ['Monday', 'Tuesday', 'Wednesday','Thusrday','Friday','Saturday','Sunday']

#Average temperature for the week
avarage_temp = np.mean(temperatures)
print ("Average:", avarage_temp)

#Highest and lowest temperattures
highest_temp = np.max(temperatures)
lowest_temp = np.min(temperatures)
print (f"Highest temperature: {highest_temp}°C")
print (f"Lowest Temperature: {lowest_temp}°C")

#Convert temperatures to Fahrenheit
Fahrenheit_list = [c*9/5+32 for c in temperatures]
print ("Fahrenheit List:", Fahrenheit_list)

#Days where the temperature was above 20°C
for i, value in enumerate(temperatures):
    if value > 20:
        print(f"{days_of_week[i]}: {value}°C")
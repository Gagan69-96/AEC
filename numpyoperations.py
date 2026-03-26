#test case 1
import numpy as np

# Weekly rainfall data in mm
rainfall = np.array([12, 15, 10, 18, 20, 14, 16])

# Calculate standard deviation
std_dev = np.std(rainfall)

print("Weekly Rainfall Data:", rainfall)
print("Standard Deviation of Rainfall:", std_dev)

#test case 2
# Monthly temperature data in degrees Celsius
temperature = np.array([25, 28, 30, 27, 26, 29, 31, 24, 23, 27, 30, 28])

# Calculate standard deviation
std_dev_temp = np.std(temperature)

print("Monthly Temperature Data:", temperature)
print("Standard Deviation of Temperature:", std_dev_temp)

#application
import numpy as np

# Daily temperature data (in °C)
temperature = np.array([30, 32, 31, 29, 33, 34, 30, 28, 35])

# Statistical calculations
mean_temp = np.mean(temperature)
median_temp = np.median(temperature)
variance_temp = np.var(temperature)
std_dev_temp = np.std(temperature)

print("Daily Temperature Data:", temperature)
print("Mean Temperature:", mean_temp)
print("Median Temperature:", median_temp)
print("Variance in Temperature:", variance_temp)
print("Standard Deviation in Temperature:", std_dev_temp)
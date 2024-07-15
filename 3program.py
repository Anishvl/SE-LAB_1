import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def tempcalfilein(path, time):
  with open(path, 'r') as file:
    values = list(map(float, file.readline().strip().split(','))) 
  temperatures = values[0] * (time ** 2) + values[1] * time + values[2]
  return temperatures

time = np.linspace(0, 10, 50)
path = "input.txt"
temp = tempcalfilein(path, time)

plt.plot(time, temp, label="File Input values")
plt.legend()
plt.xlabel('Time (hours)')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.title('Weather Modeling using Quadratic Equation (File Input)')
plt.show()
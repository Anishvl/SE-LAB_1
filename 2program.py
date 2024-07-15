import matplotlib.pyplot as plt
import numpy as np

def tempcalkey(time):
  a = float(input("Enter the value for 'a' : "))
  b = float(input("Enter the value for 'b' : "))
  c = float(input("Enter the value for 'c' : "))

  temp = a * (time ** 2) + b * time + c
  return temp

time = np.linspace(0 , 10 , 50)
temp = tempcalkey(time)

plt.plot(time , temp , label = "keyboard input values")
plt.legend()
plt.xlabel('Time')
plt.ylabel('Temperatures')
plt.grid(True)
plt.title('Weather Modelling using quadratic equation for keyboard input values')
plt.show()
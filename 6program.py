import matplotlib.pyplot as plt
import numpy as np

def temperature_calculation_hardcoded(time):
  a = 0.1
  b = -1
  c = 30

  temperature = a * (time ** 2) + b * time + c
  return temperature , (a , b , c)

def temperature_calculation_keyboardinput(time):
  a = float(input("Enter the value of 'a' : "))
  b = float(input("Enter the value of 'b' : "))
  c = float(input("Enter the value of 'c' : "))

  temp = a * (time ** 2) + b * time + c
  return temp , (a , b , c)

time_values = np.linspace(0 , 10 , 50)

temperatures1 , values1 = temperature_calculation_keyboardinput(time_values)
temperatures2 , values2 = temperature_calculation_hardcoded(time_values)

plt.plot(time_values , temperatures1 , '-r' , label = "Keyboard input" + ' : ' + ' , '.join(map(str , values1)))
plt.plot(time_values , temperatures2 , '-g' , label = 'Hard-coded coefficients' + ' : ' + ' , '.join(map(str , values2)))

plt.legend()
plt.xlabel('Time')
plt.ylabel('Temperatures')
plt.grid(True)
plt.title('Weather Modelling using quadratic equation for both hardcode and keyboard input')
plt.show()
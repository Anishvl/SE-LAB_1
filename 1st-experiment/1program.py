import matplotlib.pyplot as plt
import numpy as np

def tempcal(time):
    a = 0.1
    b = -1
    c = 30

    temp = a * (time ** 2) + b * time + c
    return temp
    
time = np.linspace(0 , 10 , 50)
temp = tempcal(time)

plt.plot(time, temp , label = "Hard-coded coefficients")
plt.legend()
plt.xlabel('Time')
plt.ylabel('Temperatures')
plt.grid(True)
plt.title('Weather Modelling using quadratic equation for Hard coded variables')
plt.show()

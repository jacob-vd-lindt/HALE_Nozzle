
# coding: utf-8

# In[5]:


#Air Density and Pressure as a Function of Altitude (Values Taken from Rocket Propulsion Elements)
# Peter Strohmaier 9/1/19
# HALE Rocket Team

import numpy as np

#Density as a Function of Altitude
def air_density(i):
    altitude = np.array([0,1000,3000,5000,10000,25000,50000,75000,100000,                     130000,160000,200000,300000,400000,600000,1000000])
    density = np.array([1.2250,1.1117,9.0912*(10**-1),7.6312*(10**-1),4.1351*(10**-1),                   4.0084*(10**-2),1.0269*(10**-3),3.4861*(10**-5),5.604*(10**-7),                   8.152*(10**-9),1.233*(10**-9),2.541*(10**-10),1.916*(10**-11),                   2.803*(10**-12),2.137*(10**-13),3.561*(10**-15)])
    return np.interp(i,altitude,density) #kg/m^3

#Ambient Pressure as a Function of Altitude
def air_pressure(i):
    altitude = np.array([0,1000,3000,5000,10000,25000,50000,75000,100000,                     130000,160000,200000,300000,400000,600000,1000000])
    pressure_ratio = np.array([1,8.8700*(10**-1),6.6919*(10**-1),5.3313*(10**-1),                              2.6151*(10**-1),2.5158*(10**-2),7.8735*(10**-4),2.0408*(10**-5),                              3.1593*(10**-7),1.2341*(10**-8),2.9997*(10**-9),8.3628*(10**-10),                              8.6557*(10**-11),1.4328*(10**-11),8.1056*(10**-13),7.4155*(10**-14)])
    x = np.interp(i,altitude,pressure_ratio)
    return x * (101325) #Pascals


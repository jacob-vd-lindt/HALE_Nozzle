
# coding: utf-8

# In[1]:


# Isentropic Nozzle Calculations for MIRA Expansion Nozzle
# Peter Strohmaier 8/26/19
# HALE Rocket Team


# Gas Dynamics Basic Parameters Calculations


import math
def metersquare_to_inchsquare(i):
    return i * 1550
def poundpersec_to_kilogrampersec(i):
    return i * 0.453592
def psi_to_Pa(i):
    return i * 6894.76

#Known Values
mdotimp = 7.72 #lb/s
mdot = poundpersec_to_kilogrampersec(mdotimp)
Mai = 0
Mat = 1

Pcimp = 350  #psi
Pc = psi_to_Pa(Pcimp)
Pe = 101325 #Pa
k = 1.228
Ta = 3600  #K
Rbar = 8314 #J/K-mol
R = 389.4145 #J/kgK

#Stagnation Point Computations
Pt = Pc*((1+((k-1)/2)*(Mai**2))**(k/(k-1)))    #Equation 4.21 Fundamentals of Gas Dynamics (FGD)
Tt = Ta*(1+((k-1)/2)*(Mai**2))                 #Equation 4.18 FGD
PresRat = Pe/Pt

#Computing Area of Throat
rt1 = math.sqrt((2/(k+1))**((k+1)/(k-1)))      #Equation 3-24 Rocket Propulsion Elements (RPE)
rt2 = math.sqrt(k*R*Ta)
At = mdot/(Pc*k*(rt1/rt2))
Atimp = metersquare_to_inchsquare(At)
Dt = 2*math.sqrt(Atimp/math.pi)

#Exit Condition Calculations
Mae = (math.sqrt(2)*math.sqrt(Pt*((Pe/Pt)**(1/k))-Pe))/(math.sqrt((k*Pe)-Pe))    #Equation 5.4 FGD
Ae = (At/Mae)*(((1+((k-1)/2)*(Mae**2))/((k+1)/2))**((k+1)/(2*(k-1))))            #Equation 5.37 FGD
exp = Ae/At
Te = Tt/(1+((k-1)/2)*(Mae**2))
TempRat = Te/Tt
Aeimp = metersquare_to_inchsquare(Ae)
De = 2*math.sqrt(Aeimp/math.pi)


print('Stagnation Pressure: ' + str(Pt) + ' Pa')
print('Stagnation Temperature: ' + str(Tt) + ' K')
print('Throat Area: ' + str(Atimp) + ' in^2')
print('Throat Diameter: ' + str(Dt) + ' in')
print('Temperature Ratio: ' + str(TempRat))
print('Pressure Ratio: ' + str(PresRat))
print('Expansion Ratio: ' + str(exp))
print('Exit Area: ' + str(Aeimp) + ' in^2')
print('Exit Diameter: ' + str(De) + ' in')
print('Exit Mach Number: '+ str(Mae))


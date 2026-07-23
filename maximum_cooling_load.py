import numpy as np

#based on governing equation Q = m * Cp * delta_T, where:
#Q = heat energy in Joules (J)
#m = mass in kilograms (kg)
#Cp = specific heat capacity in J/(kg*K)


volume_gal = 100 #volume in gallons
rho = 997 #density of water in kg/m^3
Cp = 4186 #specific heat capacity of water in J/(kg*K)

initial_temp = 21
target_temp = 5

volume_m3 = volume_gal * 0.00378541 #convert gallons to cubic meters
mass_kg = volume_m3 * rho #calculate mass in kg


delta_temp = initial_temp - target_temp #calculate temperature difference in K
Q = mass_kg * Cp * delta_temp #calculate heat energy in J

print(f"Maximum cooling load required to cool {volume_gal} gallons of water from {initial_temp}°C to {target_temp}°C is {Q:.2f} J.")
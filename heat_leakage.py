#the chiller mainly offsets heat leaking in from surroundings
# this process is ruled by eqution Q = kAT/L where:
# Q = heat energy in Joules (J)
# k = thermal conductivity of the material in W/(m*K)
# A = surface area in m^2
# T = temperature difference in K
# L = thickness of the material in m

k = 0.026
A = 3.5
L = 0.05
deltaT = 25-5
Q = k * A * deltaT / L
print(f"Heat leakage from surroundings into the cooling tub is {Q:.2f} W.")
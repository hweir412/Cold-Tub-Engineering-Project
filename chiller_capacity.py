import numpy as np

#to calulate the maximum cooling capacity required we use Q divided by time to calculate cooling power in watts

cooldown_time = 6*3600 #cooldown time in seconds (1 hour)
cooling_power = Q / cooldown_time #calculate cooling power in watts

print(f"Cooling power required to achieve the desired temperature drop in {cooldown_time} seconds is {cooling_power:.2f} W.")
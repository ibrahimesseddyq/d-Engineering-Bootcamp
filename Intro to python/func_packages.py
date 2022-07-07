##################### String Methods ##################
place = "poolhouse"
place_up= place.upper()
print(place)
print(place_up)
print(place.count("o"))
##################### List Methods #####################
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
print(areas.index(20.0))
print(areas.count(9.50))
##################### List Methods 2 ##################
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
areas.append(24.5)
areas.append(15.45)
print(areas)

areas.reverse()
print(areas)
#################### Import Package ####################
import math as m
r = 0.43
C = 2 * m.pi*r

A = m.pi* m.pow(r,2)

print("Circumference: " + str(C))
print("Area: " + str(A))
################### Selective Import ###################
r = 192500
from math import radians

dist = r * radians(12)
print(dist)
import math
radius = float(input("Radius(m):"))
height = float(input("Height(m):"))
volume = radius * radius * math.pi * height
print "Volume of cylinder =","%.1f"%volume,"m^3"

from math import pi
r=2
# area of circle up to 2 decimal places
print("Area of circle with radius", str(r), "is", round(pi*r**2,2))

# area of circle up to 4 decimal places
print("Area of circle with radius", str(r), "is", '%.4f'%(pi*r**2))

# circumference of circle upto 2 decimal places

print("Circumference of the circle with radius", str(r), "is", '%.2f'%(2*pi*r))
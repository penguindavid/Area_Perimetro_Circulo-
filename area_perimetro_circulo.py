# -*- coding: utf-8 -*-

import math

print("Área y perímetro del círculo")

# input
r = input("Digite el valor del radio: ")
r = int(r)

# processing
p = 2 * math.pi*r
a = math.pi*r*r

# output
print("...........................")
print("El área es: " + str(a))
print("El perimetro es:" + str (p))
print("...........................")

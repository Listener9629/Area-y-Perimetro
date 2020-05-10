print("Area y Perimetro de un Rectangulo".center(50,"="))
base = float(input("Base: " ))
altura = float(input("Altura: "))
area = base * altura
perimetro = 2*base + 2*altura
print(" ")
print("El area del rectangulo es: " + str(area))
print("El perimetro de rectangulo es: " + str(perimetro))
print(" ")
print("Tu rectangulo se ve de esta manera:")
print(" ")
espacio = int(((base*2)-3))

#rectangulo sin rellenar
print("* "*int(base))
for i in range(int(altura-2)):
    print(("*{}*".format(" "*int(espacio))))
print("* "*int(base))

#si quieres que el rectangulo se vea lleno
#print((("0")*int(base)+"\n")*int(altura))
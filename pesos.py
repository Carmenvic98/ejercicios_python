#Input general - peso en la tierra

peso_tierra = float(input("Por favor, ingrese su peso"))

# calculo o regla de 3 
gravedad_luna = round(peso_tierra * 1.622 / 9.81 , 2)
gravedad_mercurio = round(peso_tierra * 3.7 / 9.81 , 2)
gravedad_venus = round(peso_tierra * 8.87 / 9.81 , 2)
gravedad_marte = round(peso_tierra * 3.711 / 9.81 , 2)
gravedad_jupiter = round(peso_tierra * 24.79 / 9.81 , 2)
gravedad_saturno = round(peso_tierra * 10.44 / 9.81 , 2)
gravedad_urano = round(peso_tierra * 8.69 / 9.81 , 2)
gravedad_neptuno = round(peso_tierra * 11.15 / 9.81 , 2)

#output
print("Tu peso en la Luna es de:" + str(gravedad_luna) + "Kg.")
print("Tu peso en Mercurio es de:" + str(gravedad_mercurio) + "Kg.")
print("Tu peso en Venus es de:" + str(gravedad_venus) + "Kg.")
print("Tu peso en Marte es de:" + str(gravedad_marte) + "Kg.")
print("Tu peso en Jupiter es de:" + str(gravedad_jupiter) + "Kg.")
print("Tu peso en Saturno es de:" + str(gravedad_saturno) + "Kg.")
print("Tu peso en Neptuno es de:" + str(gravedad_neptuno) + "Kg.")
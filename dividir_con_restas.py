"""
Inserta el encabezado aquí y escribe tu código abajo
"""

# Declaraciones
cociente = 0

# Entradas
dividendo = int(input("Introduzca el dividendo: "))
divisor = int(input("Introduzca el divisor: "))

# Proceso
residuo = dividendo
while dividendo >= divisor:
    residuo -= divisor
    cociente = len(residuo)



# Salidas
print("El cociente es {cociente}")
print("El residuo es {residuo}")

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
while residuo >= divisor:
    residuo -= divisor
    cociente += 1



# Salidas
print("El cociente es {cociente}")
print("El residuo es {residuo}")

"""
Inserta el encabezado aquí y escribe tu código abajo
"""

dividendo = int(input("Introduzca el dividendo: "))
divisor = int(input("Introduzca el divisor: "))

cociente = 0
residuo = dividendo

# Proceso
while residuo >= divisor:
    residuo -= divisor
    cociente += 1

# Salidas
print(f"El cociente es {cociente}")
print(f"El residuo es {residuo}")
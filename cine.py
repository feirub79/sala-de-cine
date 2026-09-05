# Programa para gestionar la reserva de asientos de una sala de cine
# 0 = asiento libre
# 1 = asiento reservado
#David feijoo
#Declaracion de la matriz
asientos = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
# Pedir al usuario la fila y la columna del asiento que desea reservar
print("=== SISTEMA DE RESERVA DE ASIENTOS ===\n")
print("Estado inicial de la sala:")
for i in range(3):
    for j in range(4):
        print(asientos[i][j], end=" ")
    print()

print("\nLas filas van de 0 a 2 y las columnas de 0 a 3")
f = int(input("Ingrese fila (0 a 2): "))
c = int(input("Ingrese columna (0 a 3): "))

# Validación de entrada
if 0 <= f <= 2 and 0 <= c <= 3:
    # Asignar asiento
    asientos[f][c] = 1
    print(f"\n✅ Asiento en fila {f}, columna {c} reservado exitosamente.")
else:
    print("\n❌ Error: Valores de fila o columna fuera de rango.")

# Imprimir matriz actualizada
print("\nEstado de la sala:")
for i in range(3):
    for j in range(4):
        print(asientos[i][j], end=" ")
    print()
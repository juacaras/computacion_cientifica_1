import random
import matplotlib.pyplot as plt

def simular_pasajeros(n=100):
    asientos = list(range(1, n + 1))
    ocupados = set()

    asiento_primero = random.choice(asientos)
    ocupados.add(asiento_primero)

    for pasajero in range(2, n):
        if pasajero not in ocupados:
            ocupados.add(pasajero)
        else:
            asiento_libre = [a for a in asientos if a not in ocupados]
            nuevo_asiento = random.choice(asiento_libre)
            ocupados.add(nuevo_asiento)

    if 100 not in ocupados:
        asiento_100 = 100
    else:
        asiento_libre = [a for a in asientos if a not in ocupados]
        asiento_100 = random.choice(asiento_libre)

    return asiento_100


simulaciones = 1_000_000
aciertos = 0
resultados = []

for _ in range(simulaciones):
    asiento_final = simular_pasajeros()
    resultados.append(asiento_final)
    if asiento_final == 100:
        aciertos += 1


probabilidad = aciertos / simulaciones
print(f"Probabilidad de que el pasajero 100 se siente en su asiento: {probabilidad:.4f}")


plt.figure(figsize=(10, 5))
plt.hist(resultados, bins=range(1, 102), density=True, edgecolor='black', align='left')
plt.title(f'Probabilidad de asientos del pasajero 100 (1 millón de simulaciones)\n'
          f'Probabilidad de asiento 100: {probabilidad:.4f}')
plt.xlabel('Asiento en el que termina el pasajero 100')
plt.ylabel('Probabilidad')
plt.xticks(range(90, 101))
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
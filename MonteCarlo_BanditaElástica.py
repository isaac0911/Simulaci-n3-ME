# MÉTODO DE MONTE CARLO PARA UNA BANDA ELÁSTICA
# SIMULACIÓN 3; CURSO MECÁNICA ESTADÍSTICA
# Autor: Isaac Solórzano Quintana

import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la simulación
epsilon_alpha = 1
epsilon_beta = 2
N = 200
a = 1
b = 2
K = 1  # Constantes de Boltzmann (se puede usar K = 1 para simplificar)
KT_values = np.linspace(0.1, 3, 50)  # 50 valores de KT
T_values = [KT / K for KT in KT_values]  # 50 valores de T

num_steps = 10000 # Pasos para alcanzar el equilibrio

# Almacenamos la longitud promedio
lengths = []

# Función teórica para longitud media
def theoretical_length(T):
    beta = 1 / (K * T)
    P_alpha = np.exp(-beta * epsilon_alpha) / (np.exp(-beta * epsilon_alpha) + np.exp(-beta * epsilon_beta))
    P_beta = np.exp(-beta * epsilon_beta) / (np.exp(-beta * epsilon_alpha) + np.exp(-beta * epsilon_beta))
    lon_theo = N*( P_alpha * a + P_beta * b )
    return lon_theo

# Simulación de Monte Carlo
for T in T_values:

    beta = 1 / (K * T)

    # Inicializar configuraciones aleatorias (0: α, 1: β)
    configurations = np.random.choice([0, 1], size=N)

    # Inicializar la longitud total en 0
    total_length = 0

    # Equilibrio:
    for _ in range(num_steps):  # Pasos para el equilibrio
        for i in range(N):
            P_alpha = np.exp(-beta * epsilon_alpha) / (np.exp(-beta * epsilon_alpha) + np.exp(-beta * epsilon_beta))
            P_beta = np.exp(-beta * epsilon_beta) / (np.exp(-beta * epsilon_alpha) + np.exp(-beta * epsilon_beta))
            if np.random.rand() < P_alpha:
                configurations[i] = 0  # Molécula en estado α
            else:
                configurations[i] = 1  # Molécula en estado β
        for i in range(N):
            total_length += a if configurations[i] == 0 else b
    
    avg_length = total_length / num_steps
    lengths.append(avg_length)

# Calcular longitudes teóricas
theoretical_lengths = [theoretical_length(T) for T in T_values]

# Graficar resultados
plt.figure(figsize=(10, 6))
plt.plot(T_values, lengths, label='Longitud promedio (simulación)', marker='o')
plt.plot(T_values, theoretical_lengths, label='Longitud promedio (teórica)', linestyle='--')
plt.xlabel('Temperatura (T)')
plt.ylabel('Longitud promedio de la banda')
plt.title('Longitud de la banda elástica vs Temperatura')
plt.legend()
plt.grid()
plt.show()
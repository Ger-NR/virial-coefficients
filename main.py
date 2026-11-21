from src.virial import second_virial

# Parámetros del potencial
epsilon = 1
sigma = 1
mu = 1
arsigma = 1
# Límite de integración
r_max = 10 * arsigma
r_min = 0.1 * arsigma
# Temperaturas
temperatures = [10, 15, 20, 25, 30, 35, 40]

for T in temperatures:

    B, error = second_virial(T, epsilon, sigma, mu, r_max, r_min, arsigma)

    print(f"T = {T} K | B(T) = {B:.6e}")
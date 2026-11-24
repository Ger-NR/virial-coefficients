
import numpy as np
import matplotlib.pyplot as plt

from src.virial import second_virial


# ==========================================
# 1. REFERENCE PARAMETERS
# ==========================================

epsilon0 = 1
sigma0 = 1
mu0 = 1


# ==========================================
# 2. INTEGRATION LIMITS
# ==========================================

arsigma = 1

r_min = 0.1 * arsigma
r_max = 10 * arsigma


# ==========================================
# 3. TEMPERATURE INTERVAL
# ==========================================

T_values = np.linspace(5, 300, 100)


# ==========================================
# 4. BASE PARAMETERS
# ==========================================

base = {
    "epsilon": epsilon0,
    "sigma": sigma0,
    "mu": mu0,
    "r_max": r_max,
    "r_min": r_min,
    "arsigma": arsigma
}


# ==========================================
# 5. PARAMETER VARIATIONS
# ==========================================

mu_values = np.linspace(0.5 * mu0, 1.5 * mu0, 10)

sigma_values = np.linspace(0.5 * sigma0, 1.5 * sigma0, 10)

epsilon_values = np.linspace(0.5 * epsilon0, 1.5 * epsilon0, 10)


# ==========================================
# 6. CALCULATE PARAMETER SWEEP
# ==========================================

def calculate_sweep(parameter, values, base, T_values):

    curves = {}

    for value in values:

        params = base.copy()
        params[parameter] = value

        B_values = []

        for T in T_values:

            B, error = second_virial(T, **params)

            B_values.append(B)

        curves[value] = B_values

    return curves


# ==========================================
# 7. CALCULATE ALL THREE FAMILIES
# ==========================================

print("Calculating mu variations...")

mu_curves = calculate_sweep(
    "mu", mu_values, base, T_values
)

print("Calculating sigma variations...")

sigma_curves = calculate_sweep(
    "sigma", sigma_values, base, T_values
)

print("Calculating epsilon variations...")

epsilon_curves = calculate_sweep(
    "epsilon", epsilon_values, base, T_values
)


# ==========================================
# 8. CALCULATE GLOBAL Y-AXIS LIMITS
# ==========================================

all_B = []

for curves in [mu_curves, sigma_curves, epsilon_curves]:

    for B_values in curves.values():

        all_B.extend(B_values)


y_min = min(all_B)
y_max = max(all_B)

margin = 0.05 * (y_max - y_min)

global_ylim = (
    y_min - margin,
    y_max + margin
)


# ==========================================
# 9. PLOT FUNCTION
# ==========================================

def plot_curves(parameter, curves, T_values, global_ylim):

    plt.figure(figsize=(9, 6))

    for value, B_values in curves.items():

        plt.plot(
            T_values,
            B_values,
            label=f"{parameter} = {value:.4g}"
        )

    plt.xlabel("Temperature (K)")
    plt.ylabel("Second virial coefficient B(T)")
    plt.title(f"Effect of {parameter} on B(T)")

    plt.xlim(T_values[0], T_values[-1])
    plt.ylim(global_ylim)

    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    plt.show()


# ==========================================
# 10. GENERATE THE THREE GRAPHS
# ==========================================

print("Generating graphs...")

plot_curves(
    "mu",
    mu_curves,
    T_values,
    global_ylim
)

plot_curves(
    "sigma",
    sigma_curves,
    T_values,
    global_ylim
)

plot_curves(
    "epsilon",
    epsilon_curves,
    T_values,
    global_ylim
)

print("All calculations completed.")

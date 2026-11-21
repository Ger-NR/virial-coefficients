import math
from scipy.integrate import quad

from src.potential import stock_mayerBIT_perkB

def second_virial(T, epsilon, sigma, mu, r_max, r_min, arsigma):
    def integrand(r): 
        u = stock_mayerBIT_perkB(r, epsilon, sigma, mu)
        exponent =  -u / T
        return math.expm1(exponent) * r**2 # Define the integrand

    result, error = quad(integrand, r_min , r_max) # Integrates the function from 0 to r_max

    B = -2 * math.pi * arsigma**3 * result

    return B, error
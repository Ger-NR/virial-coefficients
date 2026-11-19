"""
Testing potentials

"""
from src.potential import stock_mayer6

r = 1.5
epsilon = 1.0
sigma = 1.0
miu = 0.5

u6 = stock_mayer6(r, epsilon, sigma, miu)
print("Potencial u_6: ", u6)
"""
Testing potentials

"""
from src.potential import stock_mayer6
from src.potential import stock_mayer3

r = 1.5
epsilon = 1.0
sigma = 1.0
miu = 0.5

u6 = stock_mayer6(r, epsilon, sigma, miu)
print("Potencial u_6: ", u6)

u3 = stock_mayer3(r, epsilon, sigma, miu)
print("Potencial u_3: ", u3)
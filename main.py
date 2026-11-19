"""
Testing potentials

"""
from src.potential import stock_mayerBIT
from src.potential import leonard_jones

r = 1.5
epsilon = 1.0
sigma = 1.0
miu = 0.5

uSM = stock_mayerBIT(r, epsilon, sigma, miu)
uLJ = leonard_jones(r, epsilon, sigma)

print("Potencial Stock-Mayer: ", uSM)
print("Potencial Leonard-Jones: ", uLJ)

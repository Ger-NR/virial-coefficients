import math

def stock_mayerBIT(r, epsilon, sigma, miu):
    """
    Calculates the Stock-Mayer potential
    (Leonard-Jones + Dipole-Dipole interaction)
    Note: Dipole - Dipole Contribution is based on the proposal by
    Ibarra-Tandi, B. at the "Molecular physics" curse in Autumn 2026

    u(r, epsilon, sigma, miu) =
    4*epsilon ((sigma/r)**12 - (sigma/r)**6) - miu**3/r**3

    Parameters:
    -----------
    r : float
        Intermolecular radius
    epsilon : float
        Deph of the potential well
    sigma : float
        Distance wherepotential is zero
        (or radius of the molecule)
    miu :
        Dipole-Dipole contribution coefficient
    """
    ratio = sigma/r

    potential = 4*epsilon*((ratio)**12 - (ratio)**6) - (miu**3)/(r**3)
    return potential
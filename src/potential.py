import math

def leonard_jones(r, epsilon, sigma):
    """
    Calculates the Leonard-Jones Potential

    u(r, epsilon, sigma) = 
    4*epsilon ((sigma/r)**12 - (sigma/r)**6)

    Parameters:
        -----------
        r : float
            Intermolecular radius
        epsilon : float
            Deph of the potential well
        sigma : float
            Distance where potential is zero
            (molecule radius related)
    """
    ratio = sigma/r
    potential = 4*epsilon*((ratio)**12 - (ratio)**6)
    return potential

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
        Distance where potential is zero
        (molecule radius related)
    miu : float
        Dipole-Dipole contribution coefficient
    """
    ratio = sigma/r
    potential = 4*epsilon*((ratio)**12 - (ratio)**6) - (miu**3)/(r**3)
    return potential



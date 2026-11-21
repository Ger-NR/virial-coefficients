import math

def leonard_jones_perkB(r, epsilon, sigma):
    """
    Calculates the Leonard-Jones Potential per kB using reduced units

    u(r, epsilon, sigma)/kB = 
    4*epsilon ((sigma/r)**12 - (sigma/r)**6)

    Parameters:
        -----------
        r : float
            Intermolecular radius divided by Argon's sigma
        epsilon : float
            Deph of the potential well divided by kB
        sigma : float
            Molecule radius divided by Argon's
    """
    ratio = sigma/r
    potential = 4*epsilon*((ratio)**12 - (ratio)**6)
    return potential

def stock_mayerBIT_perkB(r, epsilon, sigma, mu):
    """
    Calculates the Stock-Mayer potential per kB using reduced units
    (Leonard-Jones + Dipole-Dipole interaction)
    Note: Dipole - Dipole Contribution is based on the proposal by
    Ibarra-Tandi, B. at the "Molecular physics" curse in Autumn 2026

    u(r, epsilon, sigma, mu) =
    4*epsilon ((sigma/r)**12 - (sigma/r)**6) - mu**3/r**3

    Parameters:
    -----------
    r : float
        Intermolecular radius per Argon's sigma
    epsilon : float
        Deph of the potential well per kB
    sigma : float
        Molecule radius divided by Argon's
    mu : float
        Dipole-Dipole contribution coefficient
    """
    ratio = sigma/r
    potential = 4*epsilon*((ratio)**12 - (ratio)**6) - (mu/r)**3

    return potential



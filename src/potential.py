def stock_mayer3(r, epsilon, sigma, miu):
    """
    Calculates the Stock-Mayer potential
    (Leonard-Jones + Dipole-Dipole interaction)
    u(r, epsilon, sigma, miu) =
    4*epsilon ((sigma/r)**12 - (sigma/r)**6) - miu**2/r**3
    Parameters:
    -----------
    r : float
        Intermolecular radius
    epsilon : float
        Deph of the potential well
    sigma : float
        Distance wherepotential is zero
        (or radius of the molecule)
    """
    ratio = sigma/r

    potential = 4*epsilon*((ratio)**12 - (ratio)**6) - (miu**2)/(r**3)
    return potential

def stock_mayer6(r, epsilon, sigma, miu):
    """
    Calculates the Stock-Mayer potential
    (Leonard-Jones + Dipole-Dipole interaction)
    u(r, epsilon, sigma, miu) =
    4*epsilon ((sigma/r)**12 - (sigma/r)**6) - miu**2/r**6
    Parameters:
    -----------
    r : float
        Intermolecular radius
    epsilon : float
        Deph of the potential well
    sigma : float
        Distance wherepotential is zero
        (or radius of the molecule)
    """
    ratio = sigma/r

    potential = 4*epsilon*((ratio)**12 - (ratio)**6) - (miu**2)/(r**6)
    return potential
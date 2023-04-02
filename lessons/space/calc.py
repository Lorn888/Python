def planet_mass(graviti, radius):
    mass = (graviti*radius**2) / (6.67*10**-11)
    return mass

def planet_vol(radius):
    vol = (4*3.142*radius**2) / 3
    return vol
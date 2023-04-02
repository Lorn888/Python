from space.planet import Planet
from space.calc import planet_mass, planet_vol

Bunga = Planet('bung', 32222, 23, 'BABA')

bunga_mass = planet_mass(Bunga.gravity, Bunga.radius)
bunga_vol = planet_vol(Bunga.radius)

print(f'{Bunga.name} has a mass of {bunga_mass} and volume of {bunga_vol}')
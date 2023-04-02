class Planet:
    shape = 'round'


    def __init__(self, name, radius, graviti, system):
        self.name = name
        self.radius = radius
        self.graviti = graviti
        self.system = system
    def orbit(self):
        return f'{self.name} is orbiting in the {self.system}'

    @classmethod
    def commons(cls):
        return f'All planets are {cls.shape} because of gravity'
    @staticmethod
    def spin(speed='2000 m/h'):
        return f'The planet spins at {speed}'



Bunga = Planet('bung',32222, 23,'BABA')

print(Planet.spin('super fast'))

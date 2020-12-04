class RocketObject():
    def __init__(self, mass):
        self.mass = mass
        self.totalFuel = 0

        self.Validate()

    def Validate(self):
        if not isinstance(self.mass, int):
            raise RuntimeError('Need an integer input.')

    @property
    def Fuel(self):
        return (self.mass / 3) - 2

    @property
    def RecursiveFuel(self):
        def getFuel(value):
            value = (value / 3) - 2
            if value > 0:
                self.totalFuel += value
                getFuel(value)
            return value

        getFuel(self.mass)
        return self.totalFuel


def SolverA(rockets):
    fuelSum = 0
    for rocket in rockets:
        rocketObj = RocketObject(rocket)
        fuelSum += rocketObj.Fuel
    return fuelSum


def SolverB(rockets):
    fuelSum = 0
    for rocket in rockets:
        rocketObj = RocketObject(rocket)
        fuelSum += rocketObj.RecursiveFuel
    return fuelSum


def main():
    rockets = []

    with open('day1-inputs.txt', 'r') as f:
        for line in f.readlines():
            rockets.append(int(line.replace('\n', '')))
        f.close()
    print SolverA(rockets)
    print SolverB(rockets)
    print('Solved.')


if __name__ == '__main__':
    main()

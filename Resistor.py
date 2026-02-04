from Bus import Bus

class Resistor:

    def __init__(self, name: str, bus1: Bus, bus2: Bus, r: float):
        self.name = name
        self.bus1 = bus1
        self.bus2 = bus2
        self.r = r
        self.g = 0.0
        self.calc_g()

    def calc_g(self):
        if self.r == 0:
            raise ValueError("Resistance cannot be zero")
        self.g = 1/self.r

if __name__ == "__main__":
    R1 = Resistor("R1", "Bus1", "Bus2",100)
    print(R1.name)
    print(R1.bus1)
    print(R1.bus2)
    print(R1.r)
    print(R1.g)


from Bus import Bus

class Load:

    def __init__(self, name: str, bus1: Bus, p: float, v: float):
        self.name = name
        self.bus1 = bus1
        self.p = p
        self.v = v
        self.g = 0
        self.calc_g()

    def calc_g(self):

        if self.p == 0:
            self.g = 0.0
        else:
            self.g = self.p / (self.v ** 2)


if __name__ == "__main__":
    L1 = Load("Load1", "Bus1", 100,100)
    print(L1.name)
    print(L1.bus1)
    print(L1.p)
    print(L1.v)
    print(L1.g)

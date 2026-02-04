

class Bus:

    #Constructor
    def __init__(self, name: str):
        self.name = name  #stores our name for bus
        self.v = 0.0      #default bus voltage

    def set_bus_v(self, bus_v: float):
        self.v = bus_v

if __name__ == "__main__":
    b1 = Bus("Bus1")
    print(b1.name)
    print(b1.v)

    b1.set_bus_v(120)
    print(b1.v)
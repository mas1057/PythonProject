
from typing import Dict, List, Optional
from Bus import Bus
from Resistor import Resistor
from Load import Load
from Vsource import Vsource

class Circuit:

    def __init__(self, name: str,):
        self.name =  name
        self.buses: Dict[str, Bus] = {}
        self.resistors: Dict[str, Resistor] = {}
        self.loads: Dict[str, Load] = {}
        self.vsource: Dict[str, Vsource] = {}

        # Circuit current
        self.i = 0.0

    def add_bus(self, name: str):
        if name in self.buses:
            raise ValueError(f"bus {name} already exists")
        self.buses[name] = Bus(name)

    def add_resistor_element(self, name: str, bus1_name: str, bus2_name: str, r: float):
        try:
            bus1 = self.buses[bus1_name]
            bus2 = self.buses[bus2_name]
        except KeyError as e:
            raise ValueError(f"bus {e.args[0]} does not exist")
        self.resistors[name] = Resistor(name, bus1, bus2, r)

    def add_load_element(self, name: str, bus_name: str, p : float, v: float):
        try:
            bus = self.buses[bus_name]
        except KeyError as e:
                raise ValueError(f"bus {e.args[0]} does not exist")
        self.loads[name] = Load(name, bus, p, v)

    def add_vsource_element(self, name: str, bus_name: str, v: float):
        if name in self.vsource:
            raise ValueError(f"vsource {name} already exists")
        try:
            bus = self.buses[bus_name]
        except KeyError as e:
            raise ValueError(f"bus {e.args[0]} does not exist")
        self.vsource[name] = Vsource(name, bus, v)

    def set_i(self, i: float):
        self.i = i

    def print_nodal_voltage(self):
        print("Bus Voltages:")
        for name, bus in self.buses.items():
            print(name, "=", bus.v)

    def print_circuit_current(self):
        print("Circuit Current =", self.i)

if __name__ == "__main__":
    if __name__ == "__main__":
        c2 = Circuit("Multi-Source Test")

        c2.add_bus("A")
        c2.add_bus("B")
        c2.add_bus("C")

        c2.add_vsource_element("VS1", "A", 10.0)
        c2.add_vsource_element("VS2", "C", 5.0)

        c2.add_resistor_element("R1", "A", "B", 5.0)
        c2.add_resistor_element("R2", "B", "C", 10.0)

        c2.add_load_element("L1", "B", 8.0, 10.0)

        print("\nCircuit Name =", c2.name)
        print("Buses in circuit =", list(c2.buses.keys()))
        print("Resistors in circuit =", list(c2.resistors.keys()))
        print("Loads in circuit =", list(c2.loads.keys()))
        print("Vsources in circuit =", list(c2.vsource.keys()))
        print("Has any vsource =", len(c2.vsource) > 0)

        c2.print_nodal_voltage()
        c2.print_circuit_current()

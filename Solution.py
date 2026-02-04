from Circuit import Circuit


class Solution:
    def __init__(self, circuit: Circuit):
        self.circuit = circuit

    def do_power_flow(self):
        # Shorthand references (dicts)
        buses = self.circuit.buses
        resistors = self.circuit.resistors
        loads = self.circuit.loads
        vsources = self.circuit.vsource

        # Voltage at bus A
        vs = next(iter(vsources.values()))
        Va = vs.v
        buses["A"].set_bus_v(Va)

        # Get first resistor and load from their dicts
        rab = next(iter(resistors.values()))
        lb = next(iter(loads.values()))

        # Calculate conductances
        rab.calc_g()
        lb.calc_g()

        g_ab = rab.g
        g_load = lb.g

        # Convert conductances to resistances
        R_ab = 1.0 / g_ab
        R_load = 1.0 / g_load
        R_eq = R_ab + R_load

        # Circuit current
        I = Va / R_eq
        self.circuit.set_i(I)

        # Solve bus B voltage
        Vb = Va - I * R_ab
        buses["B"].set_bus_v(Vb)

        return Va, Vb, I

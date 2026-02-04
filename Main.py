from Circuit import Circuit
from Solution import Solution

c = Circuit("Simple Circuit")

c.add_bus("A")
c.add_bus("B")
c.add_vsource_element("VS1", "A", 100.0)
c.add_resistor_element("R1", "A", "B", 5.0)
c.add_load_element("L1", "B", 2000.0, 100.0)

Sol = Solution(c)
Va, Vb, I = Sol.do_power_flow()

c.print_nodal_voltage()
c.print_circuit_current()


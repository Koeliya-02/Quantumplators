import perceval as pcvl
import perceval.components.unitary_components as comp
import numpy as np
from math import pi
def get_CCZ() -> pcvl.Processor:
    p = pcvl.Processor("SLOS", 6)
    p.add(0, comp.BS())  # Modes (0, 1) connected to (0, 1) of the added beam splitter
    p.add([2,5], comp.BS())  # Modes (2, 5) of the processor's output connected to (0, 1) of the added beam splitter
    p.add({2:0, 5:1}, comp.BS())  # Same as above
    return p
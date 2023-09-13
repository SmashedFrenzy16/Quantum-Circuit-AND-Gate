from qiskit import *

from qiskit.visualization import plot_histogram

import numpy as n

def AND(input1, input2):

    quanc = QuantumCircuit(1, 1)

    quanc.reset(0)

    if input1 != "1" or input2 != "1":

        quanc.x(0)
    
    quanc.barrier()

    quanc.x(0)

    quanc.barrier()

    quanc.measure(0, 0)

    quanc.draw("mpl")

    sim = Aer.get_backend("qasm_simulator")

    job = execute(quanc, sim, shots=1, memory=True)

    out = job.result().get_memory()[0]

    return quanc, out

i = ["0", "1"]

j = ["0", "1"]


quanc, out = AND(i[0], j[0])

print(f"AND with inputs {i[0], j[0]} gives the output of {out}")

display(quanc.draw())

print("\n")

quanc, out = AND(i[0], j[1])

print(f"AND with inputs {i[0], j[1]} gives the output of {out}")

display(quanc.draw())

print("\n")

quanc, out = AND(i[1], j[0])

print(f"AND with inputs {i[1], j[0]} gives the output of {out}")

display(quanc.draw())

print("\n")

quanc, out = AND(i[1], j[1])

print(f"AND with inputs {i[1], j[1]} gives the output of {out}")

display(quanc.draw())

print("\n")





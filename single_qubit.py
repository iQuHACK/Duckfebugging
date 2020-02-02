'''this main code is supposed to
qi
'''
import numpy

# Importing standard Qiskit libraries and configuring account
from qiskit import QuantumCircuit, execute, Aer, IBMQ
from qiskit.compiler import transpile, assemble
from qiskit.tools.jupyter import *
from qiskit.visualization import *

# Loading your IBM Q account(s)
provider = IBMQ.load_account()

#start the code

# define the quantum circuit - initial conditions
circuit = QuantumCircuit(3, 2)
print(circuit)

# apply gates
circuit.cx(0,1)
circuit.h(0)

# measure
circuit.measure([0,1], [0,1])

# more gates
circuit.cx(1,2)
circuit.cz(0,2)
print(circuit)
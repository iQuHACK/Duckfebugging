"""
Single qubit quantum teleportation script.

Alice has a qubit in state a|0> + b|1> to be teleported to Bob.

Steps:
1. Initialize a register of 4 qubits q.
    - q[0]: Alice's original qubit
    - q[1:3]: Alice and Bob's entangled qubit
2. Entangle q[1] and q[2].
3. Perform Bell state measurement on q[0] and q[1]
4. Use the measurement result to teleport qubit
"""
from qiskit import QuantumRegister, ClassicalRegister
from qiskit import QuantumCircuit, execute, Aer, IBMQ
from qiskit.quantum_info import random_state
import numpy as np

# Load IBM account
provider = IBMQ.load_account()

# Define register of 3 qubits
q = QuantumRegister(3)
c = ClassicalRegister(2)
circuit = QuantumCircuit(q,c)

# Generate entanglement
circuit.h(1)
circuit.cx(1, 2)
circuit.barrier()

# Perform Bell state measurement
circuit.cx(0, 1)
circuit.h(0)
circuit.measure(0, 0)
circuit.measure(1, 1)

# Operate on Bob's qubit given result
circuit.cx(0, 2)
circuit.cz(1, 2)

print(circuit)
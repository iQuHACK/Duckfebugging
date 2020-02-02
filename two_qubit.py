"""
Two-qubit quantum teleportation script.

Alice has a qubit in state a|00> + b|01> + c|10> + d|11> to be teleported to 
Bob.

Steps:
1. Initialize a register of 6 qubits q.
    - q[0:2]: Alice's original qubit
    - q[2:6]: Alice and Bob's entangled qubit
2. Entangle q[2:6].
3. Perform Bell state measurement on q[0:4]
4. Use the measurement result to teleport qubit
"""
from qiskit import QuantumRegister, ClassicalRegister
from qiskit import QuantumCircuit, execute, Aer, IBMQ
from qiskit.quantum_info import random_state
from qiskit.tools.visualization import plot_state_city
import numpy as np

# Load IBM account
provider = IBMQ.load_account()

def apply_secret_unitary(secret_unitary, qubit, quantum_circuit, dagger):
    functionmap = {
                    'x':quantum_circuit.x,
                    'y':quantum_circuit.y,
                    'z':quantum_circuit.z,
                    'h':quantum_circuit.h,
                    't':quantum_circuit.t,
    }
    if dagger: functionmap['t'] = quantum_circuit.tdg    
    
    if dagger:
        [functionmap[unitary](qubit) for unitary in secret_unitary]
    else:
        [functionmap[unitary](qubit) for unitary in secret_unitary[::-1]]

secret_0 = 'hxzy'
secret_1 = 'xtyz'

# Define register of 3 qubits
q = QuantumRegister(6)
c = ClassicalRegister(6)
circuit = QuantumCircuit(q,c)

# Do things to Alice's qubit
apply_secret_unitary(secret_0, 0, circuit, False)
apply_secret_unitary(secret_1, 1, circuit, False)
circuit.barrier()

# Generate entanglement
circuit.h(2)
circuit.h(3)
circuit.cx(2, 4)
circuit.cx(3, 5)
circuit.barrier()

# Perform Bell state measurement
circuit.cx(1, 3)
circuit.cx(0, 2)
circuit.h(1)
circuit.h(0)
circuit.measure([0, 1, 2, 3], [0, 1, 2, 3])

# Operate on Bob's qubit given result
circuit.cx(3, 4)
circuit.cz(0, 4)
circuit.cx(2, 5)
circuit.cz(1, 5)
circuit.barrier()

# Do the reverse things on Bob's qubit
apply_secret_unitary(secret_0, 4, circuit, True)
apply_secret_unitary(secret_1, 5, circuit, True)

# Measure Bob's qubit
circuit.measure([4, 5], [4, 5])
print(circuit)

# Simulate circuit
simulator = Aer.get_backend('statevector_simulator')
result = execute(circuit, backend=simulator).result()
statevector = result.get_statevector(circuit)
plot_state_city(statevector)
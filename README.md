# duckfebugging's Compression and Teleportation Protocol
This is team *duckfebugging*'s repository for our project at iQuHack. The idea
is to teleport quantum data in an efficient manner. To do this we perform the
procedure in two steps:
1. compress the quantum data losslessly;
2. teleport the quantum data.

To compress quantum data, we tried to come up with a quantum version of
run-length-encoding. For simplicity, we constrained the scope of our idea into
a more manageable project of teleporting three identical qubits from Alice using
only two qubit entangled pair (four qubits for both Alice and Bob).

## Install Dependencies
To install dependencies:
```
pip install -r requirements.txt
```

## Project Structure
- `one_qubit.py`: one qubit teleportation for warmup
- `two_qubit.py`: two qubit teleportation for even more warmup
- `generalized.py`: teleportation for n-qubit

## TODO
- Algorithm for encoding a run with smaller number of qubits using Schur-Weyl
  transformation
- Algorithm for detecting runs
- Combine previous two algorithms to compress data

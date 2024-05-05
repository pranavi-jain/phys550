from qiskit.compiler import transpile

# Generating n circuits with HH added successively

def list_of_circuits(qc, n):
    # Create a list to store the circuits
    circuits = [None for x in range(n)]
    circuits[0] = qc
    num_q = qc.num_qubits

    # Generate the subsequent circuits by adding identity gates
    for i in range(1, n):
        temp = qc.copy()
        temp.h(range(0, num_q))
        temp.h(range(0, num_q))
        temp.barrier()
        temp.h(range(0, num_q))
        temp.h(range(0, num_q))
        temp.barrier()
        temp.h(range(0, num_q))
        temp.h(range(0, num_q))
        temp.barrier()

        circuits[i] = temp.copy()
        qc = temp.copy()

    return circuits


# Creating IBM job for given circuit and backend

def execute_job(circuit, backend, shots, tskip):
    circuit.measure_all()
    if not tskip:
        tqc = transpile(circuit, backend)  ## Optional - can skip transpilation
    else:
        tqc = circuit.copy()
    job = backend.run(tqc, shots=shots)
    return job

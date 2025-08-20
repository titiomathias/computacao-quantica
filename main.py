import random
import matplotlib.pyplot as plt
import numpy as np
from qutip import basis
from collections import defaultdict

def generate_bits(lenght):
    return [random.randint(0, 1) for _ in range(lenght)]


def generate_bases(lenght):
    return [random.choice(['d', 'o']) for _ in range(lenght)]


def encode_bits(bits, bases):
    qubits = []
    for bit, base in zip(bits, bases):
        if base == 'd':
            qubits.append('0' if bit == 0 else '1')
        else:
            qubits.append('d' if bit == 0 else 'o')
    else:   
        return qubits
    

def measure_qubits(qubits, bases, error_rate=0.05):
    """ Adiciona ruído ao canal quântico com probabilidade de erro """
    bits = []
    for qubit, base in zip(qubits, bases):
        if base == "d":
            measure_bit = 0 if qubit in ['0', '1'] else 1
        else:
            measure_bit = 0 if qubit in ['0', 'x'] else 1
        
        if random.random() < error_rate:
            measure_bit = 1 - measure_bit

        bits.append(measure_bit)
    else:
        return bits
        

def qberr(qubits_a, qubits_b, bases_a, bases_b):
    """ Calcula a taxa de erro quântico (QBER) entre dois conjuntos de qubits """
    errors = 0
    for qa, qb, ba, bb in zip(qubits_a, qubits_b, bases_a, bases_b):
        if ba == bb and qa != qb:
            errors += 1
    return errors / len(qubits_a) if qubits_a else 0


def sifting(bases_a, bases_b, bits_a):
    """ Realiza o processo de siftamento para manter apenas os bits medidos com bases iguais """
    sifted_bits = []
    
    for ba, bb, bit_a in zip(bases_a, bases_b, bits_a):
        if ba == bb:
            sifted_bits.append(bit_a)
    
    return sifted_bits

num_rounds = 10

bases_alice = generate_bases(num_rounds)
bases_bob = generate_bases(num_rounds)

bits_alice = generate_bits(num_rounds)

qubits = encode_bits(bits_alice, bases_alice)

bits_bob = measure_qubits(qubits, bases_bob)

# CORRIGIR CALCULO DO BIT FLIP

print("Bases de Alice:", bases_alice)
print("Bases de Bob:  ", bases_bob)
print(10*"=-=")
print("Bits de Alice:", bits_alice)
print("Bits de Bob:  ", bits_bob)
print(10*"=-=")
print("Bits Siftados:", sifting(bases_alice, bases_bob, bits_alice))
print(10*"=-=")
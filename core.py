import numpy as np

def get_sieve(limit):
    sieve = np.ones(limit + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, int(limit**0.5) + 1):
        if sieve[p]:
            sieve[p*p : limit+1 : p] = False
    return sieve

print("Math Engine: Sieve is ready.")

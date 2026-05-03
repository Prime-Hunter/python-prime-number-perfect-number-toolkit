import core
import numpy as np
from tqdm import tqdm

def main():
    print("🚀 Goldbach Mega-Scanner")
    
    limit = 100000  # Start with 100k to see it move!
    sieve = core.get_sieve(limit)
    
    results = {}
    
    # This loop uses the progress bar
    for n in tqdm(range(4, limit + 1, 2), desc="Scanning Numbers"):
        primes_to_check = np.where(sieve[:(n // 2) + 1])
        count = np.sum(sieve[n - primes_to_check])
        results[n] = count

    # Find the "winner" (the number with the most pairs)
    max_n = max(results, key=results.get)
    print(f"\n✅ Peak Found: {max_n:,} has {results[max_n]:,} pairs!")

if __name__ == "__main__":
    main()


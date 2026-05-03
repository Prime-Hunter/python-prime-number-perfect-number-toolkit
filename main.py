import core
import numpy as np

def main():
    print("--- Goldbach Conjecture Scanner ---")
    
    # Get a limit from the user
    try:
        limit = int(input("Enter the limit to scan up to: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    # Generate the sieve using our core module
    print(f"Generating primes up to {limit:,}...")
    sieve = core.get_sieve(limit)
    
    # Let's check the very last even number in your range
    n = limit if limit % 2 == 0 else limit - 1
    
    # Quick math: find partitions for n
    primes_to_check = np.where(sieve[:(n // 2) + 1])
    count = np.sum(sieve[n - primes_to_check])
    
    print(f"\nResult for {n:,}:")
    print(f"Found {count:,} unique prime pairs that sum to this number.")

if __name__ == "__main__":
    main()

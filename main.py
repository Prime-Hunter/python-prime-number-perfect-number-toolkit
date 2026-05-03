import core
import numpy as np
import csv
from tqdm import tqdm

def main():
    print("🚀 Goldbach Mega-Scanner")
    
    limit = 100000  # You can set this to 1,000,000 once you verify it works!
    sieve = core.get_sieve(limit)
    
    # We open the file here so it saves as we go
    filename = "results.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Even Number", "Partition Count"])
        
        # The Scan Loop
        for n in tqdm(range(4, limit + 1, 2), desc="Scanning Numbers"):
            # The 'vectorized' math
            primes_to_check = np.where(sieve[:(n // 2) + 1])[0]
            count = np.sum(sieve[n - primes_to_check])
            
            # Write the result to the CSV immediately
            writer.writerow([n, count])

    print(f"\n✅ Scan Complete! Data saved to {filename}")

if __name__ == "__main__":
    main()

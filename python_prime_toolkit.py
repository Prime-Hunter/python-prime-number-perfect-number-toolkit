"""
🛡️ PRIME & PERFECT NUMBER TOOLKIT - [GHOST EDITION]
-------------------------------------------------
Optimized for: Python 3.10+, Number Theory Research.
Features: Lucas-Lehmer Test, Historical Milestones, Binary Signature.
"""

import time
import sys

# Increase limit for massive numbers (up to 10 million digits)
sys.set_int_max_str_digits(10000000) 

def is_prime_basic(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def lucas_lehmer_test(p):
    if p == 2: return True
    if not is_prime_basic(p):
        print(f"⚠️  Note: {p} is not prime, so M{p} cannot be a Mersenne Prime.")
        return False
    m_p = 2**p - 1
    s = 4
    for _ in range(p - 2):
        s = (s**2 - 2) % m_p
    return s == 0

def check_historical_ghosts(p):
    """Easter Egg: Acknowledges the human history behind specific primes."""
    ghosts = {
        31:  "\n👻 [EULER'S GHOST]: Leonhard Euler verified this 10-digit giant in 1772.\n   He did it by hand. You're standing on the shoulders of a titan.",
        127: "\n✨ [THE LUCAS MILESTONE]: In 1876, Édouard Lucas verified this 39-digit prime.\n   It remained the largest known prime for 75 years. Progress is beautiful.",
        521: "\n📟 [THE SILICON DAWN]: Found in 1952. This was the first prime ever discovered\n   by a digital computer (the SWAC). The era of machines began here."
    }
    if p in ghosts:
        print(ghosts[p])

def main():
    print("--- 🛡️ Professional Prime & Perfect Number Toolkit ---")
    print("1. Find Small Primes\n2. Test Mersenne/Perfect Numbers")
    choice = input("Selection: ")

    # Easter Egg: The Answer to Life, the Universe, and Everything
    if choice == '42':
        print("\n🌌 'Perfect' numbers are like stars: rare, distant, and governed by simple laws.")
        print("The universe is 100% mathematical. Keep searching, explorer.")
        return

    if choice == '2':
        try:
            p = int(input("Enter prime exponent p: "))
            
            # Trigger Historical Ghost logic
            check_historical_ghosts(p)
            
            start_time = time.time()
            if lucas_lehmer_test(p):
                print(f"✅ SUCCESS! M{p} is a Mersenne Prime.")
                # (Save to file logic would be here)
            else:
                print(f"❌ M{p} is composite.")
            print(f"⏱️  Process took {time.time() - start_time:.4f} seconds.")
        except ValueError:
            print("Please enter a valid whole number.")

if __name__ == "__main__":
    main()

# Version ID: 01010100 01001000 01000001 01001110 01001011 01010011 
# (Spells 'THANKS' in Binary)

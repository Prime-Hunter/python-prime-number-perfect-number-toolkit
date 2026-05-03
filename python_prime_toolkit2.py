import time
import sys
import gmpy2  # High-performance math engine

def lucas_lehmer_fast(p):
    """Bypasses standard Python limits using C-based GMP math."""
    if p == 2: return True
    
    # Define the Mersenne number using gmpy2 for FFT speed
    m_p = gmpy2.pow(2, p) - 1
    s = gmpy2.mpz(4)
    
    # Progress feedback for larger exponents
    checkpoint = p // 10
    
    for i in range(p - 2):
        # The core squaring and modulo step
        s = (s * s - 2) % m_p
        
        # Optional: Print progress every 10%
        if i > 0 and i % checkpoint == 0:
            print(f"   🚀 { (i/p)*100 :.0f}% complete...")
            
    return s == 0

def main():
    print("--- 🏎️ High-Performance Prime Toolkit (gmpy2 Edition) ---")
    try:
        p = int(input("Enter a large prime exponent p (e.g., 859433): "))
        print(f"Testing M{p} using FFT-accelerated math...")
        
        start_time = time.time()
        
        if lucas_lehmer_fast(p):
            print(f"✅ SUCCESS! 2^{p}-1 is a Mersenne Prime.")
            # Note: Calculating the full perfect number for p=136M 
            # would still take massive RAM to hold in string format!
        else:
            print(f"❌ M{p} is composite.")
            
        print(f"⏱️  Calculation took {time.time() - start_time:.4f} seconds.")
        
    except ImportError:
        print("❌ Error: gmpy2 not found. Run 'pip install gmpy2' to bypass limits.")
    except Exception as e:
        print(f"⚠️  An error occurred: {e}")

if __name__ == "__main__":
    main()

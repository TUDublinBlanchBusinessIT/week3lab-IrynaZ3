# Iryna Zabolotna
# 17/02/2025
# lab3 step2

def divisors(n):

    return [i for i in range (1, n) if n % i ==0]
def isPerfectNumber (n):
    return sum(divisors(n)) == n
print(isPerfectNumber (8128))
if isPerfectNumber (8128):
    print("8128 is a perfect number")



    

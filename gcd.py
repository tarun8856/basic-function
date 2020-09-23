def gcd(a,b): 
    if a == 0: 
        return b 
    return gcd(b % a, a) 
    a = 37
    b = 78
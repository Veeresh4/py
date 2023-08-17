def gcd(a,b):
    while b:
        a,b = b, a % b
        return a
n1 = int(input())
n2 = int(input())
result = (gcd(n1,n2))
print("GCD OF :", result)
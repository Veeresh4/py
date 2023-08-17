def lcm(a,b):
    x = max(a,b)
    while True:
        if x % a == 0 and x % b == 0:
            return x 
        x += 1
n1 = int(input())
n2 = int(input())
result = lcm(n1, n2)
print("LCM of :", result)
n = int(input())
reverse = 0
while n != 0:
    i = n % 10
    reverse = reverse * 10 + i
    n //= 10
    print(reverse)
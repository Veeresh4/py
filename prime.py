n = int(input())
i = 2
count = 0
while i < n:
    if n % i == 0:
        print("Not prime")
        i += 1
        break
    else:
        print("Prime")
n = int(input())
sum = 0
temp = n
while n > 0:
    r = n % 10
    sum = sum + (r*r*r)
    n = n // 10
    if temp == sum:
        print("number is armstrong")
    else:
        print("Not armstrong number")
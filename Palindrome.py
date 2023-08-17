n = int(input())
sum = 0
temp = n
while n > 0:
    r = n % 10
    sum = (sum * 10) + r
    n = n // 10
    if temp == sum:
        print("Given num is palindrome")
    else:
        print("Given num is not palindrome")
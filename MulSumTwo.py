def MulSum(num1, num2):
    x = num1 * num2
    if x <= 500:
        return x
    else:
        return num1 + num2

num1 = int(input("enter the number :"))
num2 = int(input("enter the number :"))  
res = MulSum(num1, num2)
print("result is :", res)
num1 = float(input("Enter a number 1 :"))
num2 = float(input("Enter a number 2 :"))
op = input("Enter operator :")

if op== "+":
    print(num1+num2)
elif op=="*":
    print(num1*num2)
elif op=="-":
    print(num1-num2)
elif op=="/":
    print(num1/num2)
else:
    print("invalid operator")



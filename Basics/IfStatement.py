is_male = True
is_tall = False 

if is_male and is_tall:
    print("you are a male")
elif is_male and not(is_tall):
    print("You are a male and not tall")
elif not(is_male) and not(is_tall):
    print(" not male and not tall")
else:
    print("you are a female")


def fn_MaxNo(num1,num2,num3):
    if num1 >= num2 and num1>= num3:
        return num1
    if num2 >= num3 and num2>= num1:
        return num2
    if num3 >= num1 and num3>= num1:
        return num3
    else: 
        return 100
    
print(fn_MaxNo(3,3,3))
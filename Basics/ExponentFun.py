def RaisePower(base,power):
    result = 1
    for index in range(power):
        result = result * base
    return result

print(RaisePower(3,4))

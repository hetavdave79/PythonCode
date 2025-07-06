try:
    number = 10/0
    number =  print(int(input("Enter a number")))
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print ("not a number")
except:
    print ("Invalid input")
print("Hello")

Names = ["Hetav","Stuti","Dhyey","Mumma","Maa","Ruchi","Samir","Pranav","Mitika",1979]
print(Names)
print (Names[0])
print(Names[-1])
print(Names[-2])
print(Names[2:])
print(Names[3:6])

Names[3] = "Dheyu"


print(Names[2:])
print(Names[3:6])

Birthdates = [1,10,15,19,25,28]
Names.extend(Birthdates)
print(Names)


Names.insert(1,"Bapa")
print(Names)

#Names.sort()
#Names.reverse()

FamilyNames = Names.copy()


Names.remove("Bapa")
Names.pop

print(Names.index("Maa"))

Names.clear

## 2d lists
print ("2d lists")
numgrid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

print(numgrid[3][0])

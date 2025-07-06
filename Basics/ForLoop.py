for letter in "DhyeyDave":
    print (letter)

Family = ["Hetav","Dhyey","Stuti","Tejal"]
for  member in Family:
    print (member)

Bdates =(1,10,15,19,28)
for date in Bdates:
    print(date)   
    print(Bdates[1])

for ind in range(2,10):
    print(ind)

#Iteration through dynamic loop
Family = ["Hetav","Dhyey","Stuti","Tejal"]
for indx in range(len(Family)):
    print(Family[indx])


for indx in range(4):
    if indx == 0:
        print("First Iteration")
    else:    
        print("Not first loop") 


for i in range (10):
    print (i)


numgrid =[
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

#Nested for loops
for row in numgrid:
    print (row)
    for col in row:
        print(col)


text = "python tutorial"

for index, char in enumerate(text):
    print(index, char)

 #for index, char in "hello" -- invalid.   
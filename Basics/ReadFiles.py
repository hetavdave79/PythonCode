from pathlib import Path
#print(Path.home())

filepath = Path.home()/"MyFiles"/"MyTestFile.txt"

with open (filepath,"r")as file:
    content = file.readlines()
    for line in content:
        print(line.strip())
   # print (content)


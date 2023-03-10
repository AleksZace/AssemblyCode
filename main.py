import random
registers ={"R0":0,"R1":0,"R2":2,"R3":4,"R4":0,"R5":0,"R6":0,"R7":0,"R8":0,"R9":0,"R10":0,"R11":0,"R12":0,"PC":0}
mainMem = [random.randint(1,30) for i in range(1000)]
def ADD(R1,R2,R3):
  registers[R1] = registers[R2] + registers [R3]
  registers["PC"] +=1
def SUB(R1,R2,R3):
  registers[R1] = registers[R2] - registers[R3]
  registers["PC"] += 1 
def MOVhash(R1,mem1):
  registers[R1] = int(mem1[1:])
  registers["PC"] += 1
def MOVnohash(R1,mem1):
  registers[R1] = mainMem[int(mem1)]
  registers["PC"] += 1
def LDR(R1,mMem):
  registers[R1] = mainMem[mMem]
  registers["PC"] += 1

fileName = input("Enter filename including the format: \n")
f = open(fileName,"r")
fileAsArray = f.readlines()
newFileAsArray = []
CMP  = False
for line in fileAsArray:
  newLine = line.strip() 
  newFileAsArray.append(newLine)  
print(newFileAsArray)
for i in range(len(newFileAsArray)):
  statement = newFileAsArray[i]
  function_name, param_string = statement.split(" ", 1)
  params = [p.strip() for p in param_string.split(",")]
  if CMP == False:
    if newFileAsArray[i][0:3] == "ADD":
      ADD(params[0],params[1],params[2])
    if newFileAsArray[i][0:3] == "SUB":
      ADD(params[0],params[1],params[2])
    if newFileAsArray[i][0:3] == "MOV":
      if "#" in newFileAsArray[i]:
        MOVhash(params[0],params[1])
      else:
        MOVnohash(params[0],params[1])
    if newFileAsArray[i][0:3] == "LDR":
      LDR(params[0],params[1])
    if newFileAsArray[i][0:3] == "CMP":
      CMP  = True 
      
print(registers) 

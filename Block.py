with open("pingbici.txt") as f:
    pbc=f.readlines()
    for i in range(len(pbc)):
        pbc[i]=pbc[i].strip("\n")
Input=input()
for i in range(len(pbc)):
    if pbc[i] in Input:
        Input=Input.replace(pbc[i],"*"*len(pbc[i]))
print(Input)
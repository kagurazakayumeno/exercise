import string
import random as rd
alphabet=string.ascii_letters
times=0
Dict={}
for i in range(1,53):
    Dict[i]=alphabet[i-1]
while times<200:
    letter=""
    for i in range(0,8):
        num=rd.randint(1,52)
        letter+=Dict[num]
    print(letter)
    times+=1

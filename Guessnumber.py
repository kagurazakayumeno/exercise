import random as rd
RandomPicks=rd.randint(0,100)
i=0
i_total=0
times=1
while 1:
    inputs=int(input("please guess the number between 1 and 100: "))
    if inputs>RandomPicks:
        print("%d is too big!"%inputs)
        i+=1
    elif inputs<RandomPicks:
        print("%d is too small!"%inputs)
        i+=1
    else:
        print("%d is the right number"%inputs)
        i+=1
        print("this time u got the number after %d attempts"%i)
        i_total+=i
        Reply=input("do u wanna play again? Y/N: ")
        if Reply=="Y":
            i=0
            times+=1
            RandomPicks=rd.randint(0,100)
        else:
            aver=i_total/times
            print("on average u got the number after %.1f attempts"%aver)
            print("goodbye")
            break

import requests
import re
#Get the random number from the Internet
def random_pick():
    r=requests.get("https://python666.cn/cls/number/guess/")
    return int(r.text)
#Process the player's information
def player_info():
    try:
        f=open("record.txt")
        f.close()
    except IOError:
        f=open("record.txt","x")
        f.close()
    #Player name should fit the specifications
    while 1:
        playername=input("please enter your name: ")
        if re.match(r"[\u4e00-\u9fa5a-zA-Z]{3,12}",playername):
            break
        else:
            print("your name should only contain Chinese characters and English letters and be between 3-12 characters")
    #Get the information from the record file
    with open("record.txt","r+") as f:
        players=f.readlines()
        if players:
            i=0
            for player in players:
                i+=1
                #If existing return its information
                if re.match(r"\b%s\b"%playername,player):
                    return player
                #If not existing create a new player
                if i==len(players):
                    player=playername+" 0 0 0 0\n"
                    f.write(player)
                    return player
        #If empty create the first row
        else:
            player=playername+" 0 0 0 0\n"
            f.write(player)
            return player
#Begin to play
def play_game():
    RandomPicks=random_pick()
    player=player_info().strip()
    result=player.split(" ")
    i=0
    i_total=0
    least=0
    times=1
    while 1:
        try:
            inputs=input("please guess the integer between 1 and 100: ")
            if not re.match(r"^([1-9][0-9]{0,1}|100)$",inputs):
                raise ValueError
        except ValueError:
            print("please enter the integer between 1 and 100")
            continue
        else:
            inputs=int(inputs)
            if inputs>RandomPicks:
                print("%d is too big!"%inputs)
                i+=1
            elif inputs<RandomPicks:
                print("%d is too small!"%inputs)
                i+=1
            else:
                print("%d is the right number"%inputs)
                i+=1
                i_total+=i
                if times==1 or least>i:
                    least=i
                print("this time u got the number after %d attempts"%i)
                Reply=input("do u wanna play again? enter Y to continue, and enter any other content to quit: ")
                if Reply=="Y" or Reply=="y":
                    i=0
                    times+=1
                    RandomPicks=random_pick()
                else:
                    aver=i_total/times
                    print("u played %d times, and at least got the true answers after %d attempts. On average u got the number after %.1f attempts"%(times,least,aver))
                    print("goodbye")
                    result[1]=str(int(result[1])+1)
                    result3=(int(result[2])*float(result[3])+i_total)/(int(result[2])+times)
                    result[3]="%.1f"%result3
                    result[2]=str(int(result[2])+times)
                    if int(result[4])==0 or least<int(result[4]):
                        result[4]=str(least)
                    results=" ".join(result)
                    results=results.strip()
                    with open("record.txt","r+") as f:
                        contents=f.read()
                        contents1=contents.replace(player,results)
                    with open("record.txt","w") as f:
                        f.write(contents1)
                    break
play_game()
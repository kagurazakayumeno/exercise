f=open("report.txt","r+")
list=f.readlines()
list[0]="名次 "+list[0]
list.insert(1,"0 平均"+" 00"*11)
L=len(list)
#化成列表
for i in range(0,L):
    list[i]=list[i].strip()
    list[i]=list[i].split(" ")
list[0].extend(["总分","平均"])
#求学生总分和学生平均分
for i in range(2,L):
    total1=0
    for j in range(1,9):
        total1+=int(list[i][j])
    stu_average=total1/9
    list[i].append(str(total1))
    list[i].append(f"{stu_average:.0f}")
#排序
ele1=list.pop(0)
ele2=list.pop(0)
list.sort(key=lambda x:x[10],reverse=True)
list.insert(0,ele1)
list.insert(1,ele2)
for i in range(2,L):
    list[i].insert(0,str(i-1))
#求学科平均分
for j in range(2,13):
    total2=0
    for i in range(2,L):
        total2+=int(list[i][j])
    sub_average=total2/(L-1)
    list[1][j]=f"{sub_average:.0f}"
#替换不及格
for i in range(2,L):
    for j in range(2,10):
        if int(list[i][j])<60:
            list[i][j]="不及格"
#化为字符串列表
for i in range(0,L):
    list[i][12]+="\n"
    list[i]=" ".join(list[i])
with open("result.txt","w+") as ff:
    ff.writelines(list)
f.close

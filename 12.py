f=open("report.txt","r+")
marks=f.readlines()
marks[0]="名次 "+marks[0]
marks.insert(1,"0 平均"+" 00"*11)
L=len(marks)
#化成列表
for i in range(0,L):
    marks[i]=marks[i].strip()
    marks[i]=marks[i].split(" ")
marks[0].extend(["总分","平均"])
#求学生总分和学生平均分
for i in range(2,L):
    total1=0
    for j in range(1,10):
        total1+=int(marks[i][j])
    stu_average=total1/9
    marks[i].append(str(total1))
    marks[i].append(f"{stu_average:.0f}")
#排序
ele1=marks.pop(0)
ele2=marks.pop(0)
marks.sort(key=lambda x:x[10],reverse=True)
marks.insert(0,ele1)
marks.insert(1,ele2)
for i in range(2,L):
    marks[i].insert(0,str(i-1))
#求学科平均分
for j in range(2,13):
    total2=0
    for i in range(2,L):
        total2+=int(marks[i][j])
    sub_average=total2/(L-2)
    marks[1][j]=f"{sub_average:.0f}"
#替换不及格
for i in range(2,L):
    for j in range(2,10):
        if int(marks[i][j])<60:
            marks[i][j]="不及格"
#化为字符串列表
for i in range(0,L):
    marks[i][12]+="\n"
    marks[i]=" ".join(marks[i])
with open("result.txt","w+") as ff:
    ff.writelines(marks)
f.close()

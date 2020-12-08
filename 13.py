import re
with open("from.txt") as f:
    containing=f.read()
reply=re.findall(r"[a-zA-Z]+[a-z]",containing)
for i in range(len(reply)):
    reply[i]=reply[i]+"\n"
reply.sort()
with open("to.txt","w+") as F:
    F.write(reply)

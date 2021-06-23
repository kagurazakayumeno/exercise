import matplotlib.pyplot as plt
from collections import Counter
import json

with open('proxy.json') as f:
    data = json.loads(f.read())
port = []
for i in data:
    port.append(i['port'])
port = dict(Counter(port))
for i in port.keys():
    i = int(i)
plt.figure()
plt.bar(port)
plt.show()

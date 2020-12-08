import re
with open("english.txt") as f:
    text=f.read()
all_words=re.findall(r"\b[a-zA-Z]+\b",text)
wordnum=len(all_words)
print(f"There are %d words in words.txt."%wordnum)
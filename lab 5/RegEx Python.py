#RegEx Python

import re

#Ex1
t = input()
a = re.search("ab*", t)
print(a)

#Ex2
t = input()
x = re.search(r"ab{2,3}", t)
print(x)

#Ex3
t = input()
x = re.findall(r"[a-z_]+_[a-z]+",t)
print(x)

#Ex4
t = input()
x = re.findall(r"[A-Z][a-z]+",t)
print(x)

#Ex5
t = input()
x = re.findall(r".*a.*b$",t)
print(x)

#Ex6
t = input()
x = re.sub(r"[., ]",":",t)
print(x)

#Ex7
t = input()
x = re.sub(r"[_]","",t)
print(x)

#Ex8
t = input()
x = re.findall(r"[^A-Z]*[A-Z][^A-Z]*",t)
result = ' '.join(x)
print(result)

#Ex9
t = input()
x = re.findall(r"[A-Z][^A-Z]*",t)
res = ' '.join(x)
print(res)

#Ex10
t = input()
x = re.sub(r"(?<!^)(?=[A-Z])","_",t).lower()
print(x)
import json

data={"name":"david",
"class":"i",
"agr":6}

file=open("que2.json","r+")
n=json.load(file)
print(n)
file.close()
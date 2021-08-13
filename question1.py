import json

data={"name":"ram",
"class":"Iv",
"age":19}

file=open("que1.json","w")
json.dump(data,file)
file.close()

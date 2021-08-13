import json

data={"name":"nikita",
"class":"graduate",
"age":21}

file=open("prec1.json","w")
json.dump(data,file)
file.close()

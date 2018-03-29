import os
import json
txtfolder=os.path.abspath(os.path.join(os.getcwd(), ".."))+"\\txt"
arr=[]
for (root, dirs, files) in os.walk(txtfolder):
    for filename in files:
        path=os.path.join(root,filename)
        f = open(path, "r")
        data={"name":filename,"text":f.read()}
        arr.append(data)

with open('../json/data.json', 'w') as f:
    json.dump(arr, f)

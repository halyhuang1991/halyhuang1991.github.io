import os
import json
def setlist(str):
    ls=str.split("\t")
    ls=list(set(ls))
    return " ".join(ls)


txtfolder = os.path.abspath(os.path.join(os.getcwd(), ".."))+"\\txt"
arr = []
for (root, dirs, files) in os.walk(txtfolder):
    for filename in files:
        path = os.path.join(root, filename)
        f = open(path, "r")
        data = {"name": filename, "text": setlist(f.read()).replace("\n","<br/>"),"path":"/data/txt/"+filename}
        arr.append(data)

with open('../json/data.json', 'w') as f:
    json.dump(arr, f)

import glob
import json

items = glob.glob("./results/*")

total = 0
for item in items:
    topic = item.split('/')[2].replace('.json','')
    file = open(item,'r',encoding='utf-8')
    json_file = json.load(file)
    count = len(json_file[topic])
    total += count
    print(("{}: {}").format(item,count))
print("total is: " + str(total))    
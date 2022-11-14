import glob
import json
# test = "Bitcoin and other cryptocurrencies are a form of money that\\u2019s a stable field that the government can\\u2019t destroy and can\\u2019t distort. Because its creation is governed by the laws of mathematics. It can\\u2019t happen any faster or slower than a certain rate, and it all sort of self-adjusts.\\n\\nhttps://t.me/+sjUZEJHXqWtiMmI0\\n"

# \u2019: single quotation
# \u201c: left double quotation
# \u201d: right double quotation 
unicodes = {"\\u2019":"'", "\\n":" ", "\\u201c":"", "\\u201d":""}
files = glob.glob("./results/*")


def save_data_as_json(data, path,ensure_ascii=True):
    with open(path, "w") as f:
        json.dump(data, f, ensure_ascii=ensure_ascii)

def clean_text(sentence, unicodes):
    for key,value in unicodes.items():
        sentence = sentence.replace(key,value)
    return sentence

def extract_topic(file_name):
    return file_name.replace("./results/","").replace(".json","")

for file in files:
    with open(file, encoding="utf-8") as json_file:
        data = json.load(json_file)
        topic = extract_topic(file)
        questions = data[topic]
        for question in questions:
            for answer in question["answers"]:
                answer['content'] = clean_text(answer['content'],unicodes)
                print(answer['content'])
        path = "./cleaned_results/" + topic + ".json"
        save_data_as_json(data,path)
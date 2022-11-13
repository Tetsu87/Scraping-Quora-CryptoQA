import requests
from pprint import pprint

import datetime
import time
import csv
import json
import os


# start time
start_time = datetime.datetime.now()

# read questions form a file
file_question_topics = open("topic_list_test_a.txt", mode="r", encoding="utf-8")
topics = file_question_topics.readlines()

def get_voteCount(contents, upvote_index):
    end_index = []
    for index in upvote_index:
        end = index
        while contents[end] != "," and contents[end] != "}":
            end +=1
        end_index.append(end)
    return end_index

for topic in topics:
    quora_question_answers = {}
    topic = topic.replace("\n","")
    quora_question_answers[topic] = []

    questions_list = open("./questions/" + topic + ".txt", "r",encoding="utf-8")
    urls = questions_list.readlines()

    total = len(urls)

    count = 0
    for url in urls:
        question_answer_pair = {}
        question_answer_pair["url"] = url.replace('\n','')
        question_answer_pair["question"] = url.replace("https://www.quora.com/","").replace("-"," ").replace('\n','')
        res = requests.get(url)
        contents = res.text

        text_index = []
        upvote_index = []

        for i in range(len(contents)-14):
            text_flag = contents[i:i+7]
            upvote_flag = contents[i:i+14]
            url_flag = contents[i:i+6]

            if text_flag == '"text":':
                text_index.append(i+7)
            if upvote_flag == '"upvoteCount":':
                upvote_index.append(i+14)
        
        end_index = get_voteCount(contents, upvote_index)

        answers = []
        for i in range(len(text_index)):
            answer = {}
            answer["upvote"] = int(contents[upvote_index[i]+1:end_index[i]])
            answer["content"] = contents[text_index[i]+2:upvote_index[i]-17]
            answers.append(answer)
        
        question_answer_pair["answers"] = answers
        quora_question_answers[topic].append(question_answer_pair)

        count +=1
        if count%20 ==0:
            print(str(count) + "/"+ str(total) + " "+ str(datetime.datetime.now() - start_time))

    # save data as json format
    with open("./results/" + topic + ".json", "w") as f:
        json.dump(quora_question_answers, f, ensure_ascii=False)

# display processing time
end_time = datetime.datetime.now()
print(end_time - start_time)

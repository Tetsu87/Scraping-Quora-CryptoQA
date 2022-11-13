from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

import datetime
import time
import csv
import json

# start time
start_time = datetime.datetime.now()

# read topics form a file
file_question_topics = open("topic_list_test.txt", mode="r", encoding="utf-8")
topics = file_question_topics.readlines()

for topic in topics:

    print("starting new topic: " + str(topic))
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument('--user-data-dir=/Users/kaitetsuro/Library/Application Support/Google/Chrome/Profile 3')
    driver = webdriver.Chrome(
        chrome_options=chrome_options, executable_path="./chromedriver"
    )

    questions = []

    driver.set_window_size(1200,1000)

    driver.get("https://www.quora.com/")
    time.sleep(3)

    elem_search = driver.find_element(By.CLASS_NAME, "q-input")
    elem_search.send_keys(topic)
    time.sleep(3)

    elem_first_search_result = driver.find_element(By.ID, "selector-option-0")
    elem_first_search_result.click()

    time.sleep(3)

    win_height = driver.execute_script("return window.innerHeight")
    last_top = 1

    scroll_count = 0
    
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        # if new_height == last_height:
        #     break
        last_height = new_height
        scroll_count +=1
        time.sleep(2)

        if scroll_count == 100:
            break

    time.sleep(3)

    elem_questions = driver.find_elements(By.CLASS_NAME, "q-box.qu-borderBottom.qu-p--medium")

    with open("questions/question_list_" + topic + "2.txt", "w",encoding="utf-8") as f:
        for elem_question in elem_questions:
            elem_questions_href = elem_question.find_element(By.TAG_NAME, "a").get_attribute('href')
            f.write(elem_questions_href + "\n")

    time.sleep(2)
    print(len(elem_questions))

    driver.quit()

# end time
end_time = datetime.datetime.now()
print(end_time - start_time)

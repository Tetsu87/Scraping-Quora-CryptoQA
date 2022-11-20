from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import traceback

import datetime
import time

# start time
start_time = datetime.datetime.now()

# read topics form a file
file_question_topics = open("topic_list_test.txt", mode="r", encoding="utf-8")
topics = file_question_topics.readlines()

def flexible_sleep(stuck_count):
    if stuck_count <=5:
        return 0.5
    else:
        return stuck_count/10

for topic in topics:
    topic = topic.replace("\n","")

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

    # scroll_count = 0
    stuck_count = 0
    error_count = 0
    
    # last_height = driver.execute_script("return document.body.scrollHeight")
    # stuck_count = 0

    # scroll down 
    # while True:
    #     driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    #     time.sleep(2)
    #     new_height = driver.execute_script("return document.body.scrollHeight")
    #     if new_height == last_height:
    #         stuck_count +=1
    #         if stuck_count ==10:
    #             break
    #     stuck_count = 0
    #     last_height = new_height
    #     scroll_count +=1
    #     time.sleep(2)

    #     if scroll_count == 100:
    #         break

    while True:
        try:
            last_height = driver.execute_script("return document.body.scrollHeight")
            top = last_top

            while top < last_height:
                top += int(win_height * 0.9)
                driver.execute_script("window.scrollTo(0, %d)" % top)
                time.sleep(flexible_sleep(stuck_count))

            time.sleep(flexible_sleep(stuck_count*2))
            new_last_height = driver.execute_script("return document.body.scrollHeight")

            if last_height == new_last_height:
                time.sleep(5)
                driver.execute_script("window.scrollTo(0, %d)" % top)
                time.sleep(5)
                stuck_count +=1
            
            print(stuck_count)
        
            if stuck_count ==50:
                break
            
            last_top = last_height

            # scroll_count +=1
            # if scroll_count ==500:
            #     break

        except:
            # print("TimeoutException occurred. Save data collected so far.")
            error_count +=1
            traceback.print_exc()
            if error_count >=3:
                break
            continue

    time.sleep(3)

    elem_questions = driver.find_elements(By.CLASS_NAME, "q-box.qu-borderBottom.qu-p--medium")

    valid_num = 0
    path = "./questions/" + topic +  ".txt"
    with open(path, "w",encoding="utf-8") as f:
        for elem_question in elem_questions:
            try:
                elem_questions_href = elem_question.find_element(By.TAG_NAME, "a").get_attribute('href')
                if elem_questions_href.startswith("https://www.quora.com/"):
                    f.write(elem_questions_href + "\n")
                    valid_num +=1
            except:
                pass

    time.sleep(2)
    print("{} scraping finished!!".format(topic))
    print("Total URL numbers: " + str(len(elem_questions)))
    print("Total valid URL numbers: " + str(valid_num))

    driver.quit()

# display processing time
end_time = datetime.datetime.now()
print("\ntotal time: " + str(end_time - start_time))

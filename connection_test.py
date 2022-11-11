from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path = './chromedriver3')
driver.implicitly_wait(10)
driver.get(
    'https://www.library.chiyoda.tokyo.jp/'
)

schedule_el = driver.find_elements(By.CLASS_NAME, "schedule-list01__text")
# schedule_el = driver.find_element_by_class_name("schedule-list01__text")

print([s.text for s in schedule_el])


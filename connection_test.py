from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument(" --window-size=1920x1080")

driver = webdriver.Chrome(executable_path = './chromedriver',options=chrome_options)
driver.implicitly_wait(10)
driver.get(
    'https://www.library.chiyoda.tokyo.jp/'
)

# schedule_el = driver.find_elements(By.CLASS_NAME, "schedule-list01__text")
schedule_el = driver.find_elements(By.XPATH, '//li[@id="chiyoda-today-status"]/div/div/span')


print([s.text for s in schedule_el])


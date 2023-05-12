from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


driver = webdriver.Chrome(service=Service("/Users/ahren/Files/chromedriver_mac64/chromedriver"))
driver.get("http://python.org")

# times = []
# titles = []
# for number in range(1, 6):
#     time = driver.find_element(By.XPATH, f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{number}]/time')
#     title = driver.find_element(By.XPATH, f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{number}]/a')
#     times.append(time.text)
#     titles.append(title.text)
#     print(time.text)
#     print(title.text)
#
# dictionary = {}
# for number in range(0, 5):
#     dictionary[number] = {
#             "time": times[number],
#             "title": titles[number],
#         }
#
# print(dictionary)

times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
titles = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

for time in times:
    print(time.text)

for title in titles:
    print(title.text)


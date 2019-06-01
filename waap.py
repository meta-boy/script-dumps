# Note: whatsapp automated birthday wishing shit app
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime


name = input("Name of the user you want to wish happy birthday: ")

# browser = webdriver.Chrome("/home/source/Downloads/chromedriver")

browser = webdriver.Chrome("path/to/chromedriver")


browser.get("https://web.whatsapp.com")

time.sleep(20)

search = browser.find_elements_by_xpath(
    "//input[@title='Search or start new chat']")[0]
search.send_keys(name + Keys.ENTER)


# Change your message here

message = """
♪ღ♪*•.¸¸¸.•*¨¨*•.¸¸¸.•*•♪ღ♪¸.•*¨¨*•.¸¸¸.•*•♪ღ♪•*
♪ღ♪░H░A░P░P░Y░ B░I░R░T░H░D░A░Y░░♪ღ♪
*•♪ღ♪*•.¸¸¸.•*¨¨*•.¸¸¸.•*•♪¸.•*¨¨*•.¸¸¸.•*•♪ღ♪•« 

"""

# Might cause some issues, because I use whatsa;; business

search = browser.find_elements_by_xpath("//div[@class='_13mgZ']")[0]
text = browser.find_elements_by_xpath("//div[@class='_13mgZ']")[0]
search.click()
time.sleep(1)
# print(search) debugging 101

# A bit hacky here

while True:
    a = datetime.datetime.now()
    if a.hour == 0 and a.minute == 0 and a.second == 0:
        text.send_keys(message)
        text.send_keys(Keys.ENTER)
        break

browser.quit()

from selenium import webdriver
import time
from bs4 import BeautifulSoup

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("https://www.youtube.com/channel/UCYO_jab_esuFRV4b17AJtAw/videos")
pageHeight = 0
newPageHeight = 0

while(pageHeight != newPageHeight):
    pageHeight = newPageHeight
    newPageHeight = driver.execute_script("return document.getElementById('content').scrollHeight;")
    if pageHeight != newPageHeight:
        driver.execute_script("window.scrollTo(0," + newPageHeight + ");")
        time.sleep(4)

soup = BeautifulSoup(driver.page_source, "html.parser")

"""text_file = open("C:/Users/jlbic/Desktop/output.txt", "w", encoding="utf-8")
text_file.write(driver.page_source)
text_file.close()"""
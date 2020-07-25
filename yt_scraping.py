import requests
import time
from selenium import webdriver
from bs4 import BeautifulSoup


def soupFromInfiniteScroller(url):
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.get(url)
    pageHeight = 1
    newPageHeight = 0

    while (pageHeight != newPageHeight):
        pageHeight = newPageHeight
        newPageHeight = driver.execute_script("return document.getElementById('content').scrollHeight;")
        if pageHeight != newPageHeight:
            driver.execute_script("window.scrollTo(0," + str(newPageHeight) + ");")
            time.sleep(4)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()
    return soup


def soupFromURL(url):
    try:
        page = requests.get(url)
        return BeautifulSoup(page.content, "html.parser")
    except:
        print("could not retrieve soup object from URL")


def cutStringFromText(text, stringBefore, stringAfter):
    wantedString = text.partition(stringBefore)[2]
    wantedString = wantedString.partition(stringAfter)[0]
    return wantedString


# Takes Soup from the "All Videos" tab of a Youtube Channel, returns URL's of the listed videos on that Page
def vidURLsFromChannelSoup(soup):
    containers = soup.find_all("h3")
    urls = []
    for container in containers:
        try:
            aTag = container.find("a")
            urls.append("https://www.youtube.com" + aTag.attrs["href"])
        except:
            print("no a-tag found")

    return urls


def vidLikesFromSoup(soup):
    return cutStringFromText(soup.text, "likeCount\\\":", ",\\\"likeCountText")


def vidDislikesFromSoup(soup):
    return cutStringFromText(soup.text, "dislikeCount\\\":", ",\\\"dislikeCountText")


def vidDurationsFromSoup(soup):
        metadataText = soup.find("div", {"id": "player-api"}).find_next().find_next().text
        try:
            return cutStringFromText(metadataText, "u0026dur=", "\\\\")
        except:
            return "no data"


def vidDescriptionFromSoup(soup):
    try:
        description = soup.find("p", {"id": "eow-description"})
        return description.text
    except:
        return "could not retrieve description"


def vidDateFromSoup(soup):
    try:
        return cutStringFromText(soup.text, "publishDate\\\":\\\"", "\\\",\\\"ownerChannelName")
    except:
        return "no Data"

"""
text_file = open("C:/Users/jlbic/Desktop/output.txt", "w", encoding="utf-8")
text_file.write(text)
text_file.close()

def convertStringToTimeInSeconds(string):
    total_seconds = 0

    if len(string) > 5:
        time_data = datetime.strptime(string, '%H:%M:%S')
    else:
        time_data = datetime.strptime(string, '%M:%S')

    total_seconds = time_data.second + time_data.minute * 60 + time_data.hour * 3600
    return total_seconds
"""
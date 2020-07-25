import pandas as pd
import yt_scraping as yt
import matplotlib.pyplot as plt
import time

cgpSoup = yt.soupFromInfiniteScroller("https://www.youtube.com/user/BibisBeautyPalace/videos")
URLs = yt.vidURLsFromChannelSoup(cgpSoup)
dataset = {"uploadDate": [], "duration": []}
counter = 0

for URL in URLs:
    soup = yt.soupFromURL(URL)
    dataset["uploadDate"].append(yt.vidDateFromSoup(soup))
    dataset["duration"].append(yt.vidDurationsFromSoup(soup))
    print("scraped video " + str(counter))
    counter += 1
    time.sleep(0.5)

df = pd.DataFrame.from_dict(dataset)
print(df)
df.to_csv("bibi.csv", encoding='utf-8', index=False)
import requests, urllib
# import http.client
from pathlib import Path
# from datetime import datetime
import pandas as pd
from bs4 import BeautifulSoup

class fetchResults:
    def __init__(self,years:list,url: str,columns:list):
        self.yearS=years
        self.urL=url
        self.columnS=columns
    def results(self):
        years=self.yearS
        url=self.urL
        columns=self.columnS
        rows = []
        for year in years:
            # Get the requests using the request class
            page = requests.get(url + year)
            # using the beautiful soup to get the content
            soup = BeautifulSoup(page.content, "html.parser")
            # Get all div html tags and class archives
            divs = soup.findAll("div", attrs={"class": "archives"})
            for div in divs:
                row = {}
                # Get the day using this and store
                day = div.find("a", attrs={"class": "title"}).find("span").text
                row[columns[0]] = day
                # The dat was in the format "Monday24th January 2000" so had to replace "Monday" with "",
                a = (div.find("a", attrs={"class": "title"}).text).replace(day, "")
                # Split ther remaining 24th Januray 2000 in to seperate woirds to a temporary list
                temp = a.split(" ")

                # Take out the "th" from the date numbers
                temp[0] = temp[0][1:]
                th = temp[0].replace("th", "")
                st = th.replace("st", "")
                row[columns[1]] = st.replace("rd", "")
                # print(temp[0].replace("th",""))
                # Store month and year
                row[columns[2]] = temp[1]
                row[columns[3]] = temp[2]

                lis = div.findAll("li", attrs={"class": "new ball"})
                num = 4
                for li in lis:
                    row[columns[num]] = li.text
                    num += 1
                lis2 = div.findAll("li", attrs={"class": "new lucky-star"})
                num = 9
                for li in lis2:
                    row[columns[num]] = li.text
                    num += 1
                rows.append(row)
        return pd.DataFrame(rows)
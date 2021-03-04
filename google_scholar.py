from bs4 import BeautifulSoup
import json
import requests
import time 





years = [
    2010,
    2011,
    2012,
    2013,
    2014,
    2015,
    2016,
    2017,
    2018,
    2019,
    2020,
]

keywords = "nanodelivery systems AND in vitro digestion"
headers= {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36"
}
for y in years: 
    keywords = keywords.replace(" ", "+")
    print(keywords)
    r = requests.get(f"https://scholar.google.com/scholar?hl=pt-BR&as_sdt=0%2C5&as_ylo={y}&as_yhi={y}&as_vis=1&q={keywords}", headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")
    print(r.content)
    total = soup.select(".gs_ab_mdw")[1].get_text()
    print(y, total.split(" ")[1]) 
    time.sleep(1)
   
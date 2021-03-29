import requests 
import json
year_pairs = [
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
keywords="nano delivery systems AND in vitro digestion"
for y in year_pairs: 
    keywords = keywords.replace(" ", "+")
    r = requests.get(f"https://api.crossref.org/works?query={keywords}&filter=from-created-date:{y},until-created-date:{y}")
    result = json.loads(r.text)
    print(y,  result["message"]["total-results"])


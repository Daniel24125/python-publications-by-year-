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
keywords="'Bioactive OR compounds OR Bioaccessibility'"
for y in year_pairs: 
    r = requests.get(f"https://api.crossref.org/works?query={keywords}&filter=from-created-date:{y},until-created-date:{y}")
    # r = requests.get(f"https://scholar.google.com/scholar?q=Bioaccessibility&hl=pt-BR&as_sdt=0%2C5&as_vis=1&lookup=0&as_ylo=2005&as_yhi=2005")
    result = json.loads(r.text)
    print(y,  result["message"]["total-results"])


import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/90.0.4430.212 Safari/537.36",
    "Accept-Language": "en-US, en;q=0.5",
}


def getdata(url):
    r = requests.get(url, headers=HEADERS)
    return r.text


def html_code(url):
    htmldata = getdata(url)
    soup = BeautifulSoup(htmldata, "html.parser")
    return soup


def cus_rev(soup):
    data_str = ""
    for item in soup.find_all("p", class_="pre-white-space"):
        data_str = data_str + item.get_text()
    result = data_str.split("\n")
    return result


rev_result = [""]
for i in range(275):
    print(i)
    url = f"https://www.bestbuy.com/site/reviews/apple-watch-nike-series-7-gps-45mm-midnight-aluminum-case-with-anthracite-black-nike-sport-band-midnight/5706680?variant=A&skuId=5706680&page={i}"
    soup = html_code(url)
    rev_data = cus_rev(soup)
    for i in rev_data:
        if i == "":
            pass
        else:
            rev_result.append(i)

# write to file
with open("bestbuy4.txt", "w", encoding="utf-8") as f:
    for i in rev_result:
        f.write(i + "\n")

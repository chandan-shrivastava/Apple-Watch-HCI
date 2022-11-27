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
    rows = soup.find_all("div", attrs={"class": "col _2wzgFH K0kLPL"})
    allrev = []
    for row in rows:
        sub_row = row.find_all("div", attrs={"class": "row"})
        review = sub_row[1].find_all("div")[2].text
        allrev.append(review)
        # print(f"{review}")
        break
    return allrev


rev_result = []
for i in range(100):
    url = f"https://www.flipkart.com/apple-watch-se-gps-40mm-gold-aluminium-case-starlight-sport-band-regular/product-reviews/itm95c1d8b0f316b?pid=SMWG6VNR6QE87QYY&lid=LSTSMWG6VNR6QE87QYYJAV113&marketplace=FLIPKART&page={i}"
    soup = html_code(url)
    rev_data = cus_rev(soup)
    if rev_data == "":
        break
    for i in rev_data:
        if i == "":
            pass
        else:
            rev_result.append(i)

for i in range(100):
    url = f"https://www.flipkart.com/apple-watch-series-3-gps-42mm-space-grey-aluminium-case-black-sport-band/product-reviews/itm91c560e722cdd?pid=SMWF94AYMNYHTYDJ&lid=LSTSMWF94AYMNYHTYDJFOPINH&marketplace=FLIPKART&page={i}"
    soup = html_code(url)
    rev_data = cus_rev(soup)
    if rev_data == "":
        break
    for i in rev_data:
        if i == "":
            pass
        else:
            rev_result.append(i)

with open("flipkart.txt", "w", encoding="utf-8") as f:
    for i in rev_result:
        f.write(i + "\n")

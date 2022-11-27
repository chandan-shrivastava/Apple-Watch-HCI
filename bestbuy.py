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
for i in range(18):
    print(i)
    url = f"https://www.bestbuy.com/site/reviews/apple-watch-series-8-gps-45mm-midnight-aluminum-case-with-midnight-sport-band-m-l-midnight/6340256?variant=A&skuId=6340256&page={i}"
    soup = html_code(url)
    rev_data = cus_rev(soup)
    for i in rev_data:
        if i == "":
            pass
        else:
            rev_result.append(i)

for i in range(12):
    print(i)
    url = f"https://www.bestbuy.com/site/reviews/apple-watch-series-8-gps-41mm-starlight-aluminum-case-with-starlight-sport-band-s-m-starlight/6340250?variant=A&skuId=6340250&page={i}"
    soup = html_code(url)
    rev_data = cus_rev(soup)
    for i in rev_data:
        if i == "":
            pass
        else:
            rev_result.append(i)

for i in range(7):
    print(i)
    url = f"https://www.bestbuy.com/site/reviews/apple-watch-series-8-gps-45mm-midnight-aluminum-case-with-midnight-sport-band-s-m-midnight/6340255?variant=A&skuId=6340255&page={i}"
    soup = html_code(url)
    rev_data = cus_rev(soup)
    for i in rev_data:
        if i == "":
            pass
        else:
            rev_result.append(i)

for i in range(13):
    print(i)
    url = f"https://www.bestbuy.com/site/reviews/apple-watch-ultra-gps-cellular-49mm-titanium-case-with-midnight-ocean-band-titanium/6339708?variant=A&skuId=6339708&page={i}"
    soup = html_code(url)
    rev_data = cus_rev(soup)
    for i in rev_data:
        if i == "":
            pass
        else:
            rev_result.append(i)

for i in range(10):
    print(i)
    url = f"https://www.bestbuy.com/site/reviews/apple-watch-ultra-gps-cellular-49mm-titanium-case-with-green-alpine-loop-medium-titanium/6339711?variant=A&skuId=6339711&page={i}"
    soup = html_code(url)
    rev_data = cus_rev(soup)
    for i in rev_data:
        if i == "":
            pass
        else:
            rev_result.append(i)

# write to file
with open("bestbuy.txt", "w", encoding="utf-8") as f:
    for i in rev_result:
        f.write(i + "\n")

from operator import contains
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
    for item in soup.find_all("div", class_="a-row a-spacing-small review-data"):
        data_str = data_str + item.get_text()
    result = data_str.split("\n")
    return result


rev_result = []
for i in range(100):
    print(i)
    url = f"https://www.amazon.in/Apple-Watch-Starlight-Aluminium-Sport/product-reviews/B0BDKHQ5W1/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews&pageNumber={i}"
    soup = html_code(url)
    rev_data = cus_rev(soup)
    if rev_data == [""]:
        break
    for i in rev_data:
        if i == "" or i.__contains__("The media could not be loaded."):
            pass
        else:
            rev_result.append(i)

for i in range(100):
    print(i)
    url = f"https://www.amazon.in/Apple-Watch-Cellular-Silver-Aluminium/product-reviews/B0BDK37XQ6/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews&pageNumber={i}"
    soup = html_code(url)
    rev_data = cus_rev(soup)
    if rev_data == [""]:
        break
    for i in rev_data:
        if i == "" or i.__contains__("The media could not be loaded."):
            pass
        else:
            rev_result.append(i)

for i in range(100):
    print(i)
    url = f"https://www.amazon.in/Apple-Watch-GPS-Cellular-40mm/product-reviews/B09G9717T5/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews&pageNumber={i}"
    soup = html_code(url)
    rev_data = cus_rev(soup)
    if rev_data == [""]:
        break
    for i in rev_data:
        if i == "" or i.__contains__("The media could not be loaded."):
            pass
        else:
            rev_result.append(i)


with open("amazon.txt", "w", encoding="utf-8") as f:
    for i in rev_result:
        f.write(i + "\n")

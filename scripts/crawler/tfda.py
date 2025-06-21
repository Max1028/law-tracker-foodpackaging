import requests
from bs4 import BeautifulSoup

def fetch_tfda_laws():
    url = "https://www.fda.gov.tw/TC/siteList.aspx?sid=10053"
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, "html.parser")

    items = []
    for row in soup.select(".table01 tbody tr"):
        cols = row.find_all("td")
        if len(cols) < 2:
            continue
        date = cols[0].get_text(strip=True)
        title = cols[1].get_text(strip=True)
        link = cols[1].find("a")["href"] if cols[1].find("a") else ""
        if not link.startswith("http"):
            link = "https://www.fda.gov.tw" + link
        items.append({
            "source": "TFDA",
            "title": title,
            "date": date,
            "link": link,
            "content": ""  # 可擴充為內頁內容擷取
        })
    return items

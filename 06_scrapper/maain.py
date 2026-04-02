import requests
from bs4 import BeautifulSoup
import sys

sys.stdout.reconfigure(encoding="utf-8")

keyword = "파이썬"
url = f"https://search.incruit.com/list/search.asp?col=job&kw={keyword}&startno=0"

response = requests.get(url)
response.encoding = response.apparent_encoding
soup = BeautifulSoup(response.text, "html.parser")

lis = soup.find_all("li", class_="c_col")
jobs = []

for li in lis:
    company = li.find("a", class_="cpname").get_text(strip=True)
    a_tag = li.find("div", class_="cell_mid").find("a")
    title = a_tag.get_text(strip=True)
    href = a_tag["href"]
    location = li.find("div", class_="cl_md").find_all("span")[0].get_text(strip=True)

    # print(company)
    # print(title)
    # print("-" * 30)
    print(location)

    job_data = {
        "title": title,
        "company": company,
        "location": location,
        "href": href
    }

    jobs.append(job_data)

print(jobs)
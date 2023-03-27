from bs4 import BeautifulSoup
from lxml import etree
import requests


URL = "http://film.iksv.org/en/the-42nd-istanbul-film-festival-2023/alice-darling"
webpage = requests.get(URL)
soup = BeautifulSoup(webpage.content, "html.parser")
dom = etree.HTML(str(soup))

print(dom.xpath('//*[@id="content"]/article/section[1]/div/div[3]/div/p[2]'))
for elem in soup.find_all("p"):
    print(elem)
    print()

print(soup.find_all("h6")[-1].text)
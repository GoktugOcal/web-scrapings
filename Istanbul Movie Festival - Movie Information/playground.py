from bs4 import BeautifulSoup
from lxml import etree
import requests


URL = "https://film.iksv.org/en/the-42nd-istanbul-film-festival-2023/the-march-on-rome"
webpage = requests.get(URL)
soup = BeautifulSoup(webpage.content, "html.parser")
dom = etree.HTML(str(soup))

elem = dom.xpath('//*[@id="content"]/article/section[1]/div/div[3]/div/h2')
print(elem[0].findall("i")[0].text)

exit()
for elem in soup.find_all("p"):
    print(elem)
    print()

print(soup.find_all("h6")[-1].text)
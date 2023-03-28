from bs4 import BeautifulSoup
from lxml import etree
import requests

import multiprocessing
import time
import json

def movie_info_scrapper(movie):
    print(movie["movie_name"])
    webpage = requests.get(movie["movie_page_url"])
    soup = BeautifulSoup(webpage.content, "html.parser")
    dom = etree.HTML(str(soup))
    try:
        # awards = driver.find_element(By.XPATH, '//*[@id="content"]/article/section[1]/div/div[3]/div/p[1]/strong').text
        movie["awards"] = dom.xpath('//*[@id="content"]/article/section[1]/div/div[3]/div/p[1]/strong')[0].text
    except:
        movie["awards"] = None

    elem = dom.xpath('//*[@id="content"]/article/section[1]/div/div[3]/div/h2')
    if elem:
        orig_name = elem[0].findall("i")

        if orig_name: movie["original_name"] = orig_name[0].text
        else: movie["original_name"] = movie["movie_name"]
    else: movie["original_name"] = movie["movie_name"]
    

    movie["description"] = soup.find_all("p")[-4].text
    movie["section"] = soup.find_all("h6")[-1].text

    return movie

    # try:
    #     # movie["description"] = driver.find_element(By.XPATH, '//*[@id="content"]/article/section[1]/div/div[3]/div/p[2]').text
    #     movie["description"] = dom.xpath('//*[@id="content"]/article/section[1]/div/div[3]/div/p[2]')[0].text
    # except:
    #     try:
    #         # movie["description"] = dom.xpath('//*[@id="content"]/article/section[1]/div/div[3]/div/p[1]')[0].text
    #         movie["description"] = soup.find_all("p")[-4].text
    #     except:
    #         movie["description"] = None



# for movie in all_movie_list:
#     movie_info_scrapper(movie)

if __name__ == "__main__":

    with open("data/movies.json", "r", encoding='utf8') as f:
        all_movie_list = json.loads(f.read())

    # multiprocessing.freeze_support()
    pool = multiprocessing.Pool()
    pool = multiprocessing.Pool(processes=32)
    all_movie_list = pool.map(movie_info_scrapper, all_movie_list)

    with open("data/movies.json", "w", encoding='utf8') as f:
        f.write(json.dumps(all_movie_list, indent=4))
        print("JSON created...")
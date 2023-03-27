from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from bs4 import BeautifulSoup
from lxml import etree
import requests

import multiprocessing
import time
import json


    

def movie_title_director_scrapper(driver):
    li = []
    elements = driver.find_elements(By.CLASS_NAME, 'boxContainer')
    for box in elements:
        texts = box.find_element(By.CLASS_NAME, 'texts')
        movie_name = texts.find_element(By.TAG_NAME, 'strong').text
        director = texts.find_element(By.TAG_NAME, 'span').text
        # page_url = texts.find_element(By.XPATH, '//*[@id="content"]/article/section/div/div[1]/div[1]/div[2]/div[2]/ul/li[1]/a').get_attribute('href')
        page_url = texts.find_element(By.TAG_NAME, 'a').get_attribute("href")
        li.append({"movie_name" : movie_name, "director" : director, "movie_page_url" : page_url})
    return li
url = 'https://film.iksv.org/en/programme'

options = webdriver.ChromeOptions()

 
driver = webdriver.Chrome(
    service=ChromeService( 
	    ChromeDriverManager().install()
        )
    ) 
 
driver.get(url)

all_movie_list = []
while(True):
    page_movie_list = movie_title_director_scrapper(driver)
    all_movie_list += page_movie_list
    element = driver.find_element(By.CLASS_NAME, 'next')
    html = element.get_attribute("class")
    if "current" in html: break
    # print(driver.current_url)
    element.click()
    print("Clicked.")
    time.sleep(5)
    # wait = WebDriverWait(driver, 30)
    # wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/article/section/div/div[1]/div[1]/div[2]')))

driver.close()

with open("movies.json", "w", encoding='utf8') as f:
    f.write(json.dumps(all_movie_list, indent=4))
    print("JSON created...")
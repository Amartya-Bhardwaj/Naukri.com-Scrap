from bs4 import BeautifulSoup, element
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv

driver = webdriver.Chrome(ChromeDriverManager().install())
wait = WebDriverWait(driver, 20)

a = str(input("ENter movie Name: "))
params = {'q',a}
driver.get("https://www.google.com/search?q="+a)
time.sleep(3)
soup = BeautifulSoup(driver.page_source,'html.parser')
soup.prettify()

result = soup.find(class_='I6TXqe')
imdb_res = result.find_all('div',class_='osrp-blk')
for i in imdb_res:
    ans = i.find('h2',class_='qrShPb kno-ecr-pt PZPZlf mfMhoc')
    imdb = i.find('span',class_='gsrt IZACzd')
    print('Name: '+ans.text)
    print('IMDB:'+imdb.text)

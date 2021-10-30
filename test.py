# Install selenium using command " pip install selenium "
from bs4 import BeautifulSoup
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

# Update the URL of Naukri Page! ( Make Sure that the page link which you're putting must be a job listing page and it must have Next page buttons. )
driver.get("https://www.naukri.com/cloud-developer-jobs")
time.sleep(3)
soup = BeautifulSoup(driver.page_source,'html.parser')
driver.close()
df = pd.DataFrame(columns=['Title'])
result = soup.find(class_='list')
job_els = result.find_all('article',class_='jobTuple bgWhite br4 mb-8')
#result2 = soup.find(class_='')
csv_file = open('Naukri.csv', 'a', encoding="utf-8", newline='')
csv_writer = csv.writer(csv_file)
# Writing the Heading of CSV file.
csv_writer.writerow(['Title','Skills'])
i=0
for job_el in job_els:
    Title = job_el.find('a',class_='title fw500 ellipsis')
    skills = job_el.find('ul',class_='tags has-description')
    print(Title.text+'\n'+skills.text)
    i+=1
    print('------------------------------------------'+str(i)+'--------------------------------------------')
    csv_writer.writerow([Title.text,skills.text])

csv_file.close()
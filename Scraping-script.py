from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
import csv

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://threatmap.bitdefender.com/')
# sleep(60)
while(1):
    res = driver.execute_script("return document.documentElement.outerHTML")
    soup = BeautifulSoup(res,'lxml')
    tags = soup.find_all('tbody',{'id':'attacks_data'})
    tags = tags[0]
    for tr in tags.find_all('tr'):
        # sleep(1)
        print(tr.contents,end='\n')
        with open("attacks.csv",'a+',newline='') as f:
            writer = csv.writer(f,delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
            if len(list(tr.contents)) == 5:
                writer.writerow(list(tr.contents))
    sleep(20)
driver.quit()

# This script is written to scrape the data from a dynamic website.
# A dynamic website is a site that contains dynamic pages such as templates,
# contents, scripts etc. In a nutshell, the dynamic website displays various
# content types every time it is browsed. The web page can be changed with the
# reader that opens the page, character of consumer interplay, or day time.
# Or, Dynamic website is a website in which the data changes very frequently.

from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
import csv

# Below code is to automate Chrome only if you want to automate mozilla you have
# to download geckodriver according to the version you are using of mozilla.
# Just download the geckodriver and place it in the directory
# and replace 'chromedriver.exe' with the geckodriver in below line.
# Or, you can simple uncomment the line 12 and comment the line 11.
driver = webdriver.Chrome(executable_path='chromedriver.exe')
# driver = webdriver.Mozilla(executable_path='geckodriver.exe')

driver.get('https://threatmap.bitdefender.com/') # Opens the link in the browser.
sleep(60) # It gives the website sufficiant time to load all its content.
while(1):
    # Executes the javascript to get the HTML everytime it is executes without
    # refreshing the website, since we are scraping the dynamic website it is
    # very important to prevent refreshing of website, since the data will not
    # be availabe as we wanted.
    res = driver.execute_script("return document.documentElement.outerHTML")

    # To convert the response of the above line to readable html.
    soup = BeautifulSoup(res,'lxml')
    # It find the table-body('tbody') tag since we want the data from the table
    # which is updating regularly and the id of the table is 'attacks_data'.
    # In futue it can change since website is maintained regularly so you can
    # change the below body tag and id tag accordingly.
    tags = soup.find_all('tbody',{'id':'attacks_data'})
    tags = tags[0] # We just want first table.

    for tr in tags.find_all('tr'): # Iterate over the all the rows in the table.
        print(tr.contents,end='\n') # Prints the content of the row in form of list.

        # To Collect the data we use 'csv' module to write in csv file.
        with open("attacks.csv",'a+',newline='') as f:
            writer = csv.writer(f,delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
            if len(list(tr.contents)) == 5: # we want that data only which has all the 5 columns data.
                writer.writerow(list(tr.contents)) # Writes the row to the csv file.

    sleep(20)
driver.quit() # When you're done just press cntrl+c to quit and the browser will get close.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd
from datetime import datetime
import os
import sys

now = datetime.now()
# DDMMYYYY
day_month_year = now.strftime("%d%m%Y")

website = 'https://es.investing.com/news/most-popular-news'
path = './chromedriver_linux64/chromedriver'

# headless-mode
options = Options()
options.add_argument('--headless')

service = Service(executable_path=path)
driver = webdriver.Chrome(service = service,options = options)
driver.get(website)

containers = driver.find_elements(by="xpath", value='//div[@class="largeTitle"]/article/div[@class="textDiv"]')

titles = []
subtitles = []
links = []

for container in containers:
    title = container.find_element(by="xpath", value='./a[@class="title"]').text
    subtitle = container.find_element(by="xpath", value='./p').text
    link = container.find_element(by="xpath", value='./a').get_attribute("href")
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)

my_dict = {
    'titles': titles,
    'subtitles' : subtitles,
    'links' : links
}

df_headlines = pd.DataFrame(my_dict)
filename=f'headline-{day_month_year}.csv'
df_headlines.to_csv(filename)

driver.quit()


from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


"""search=input("Enter the element to be searched: ")
search=search.replace(" ","+")"""

search="coffee shop near me"
content="https://www.google.com/search?q="+search+"&start=0"
r=requests.get(content)
soup=BeautifulSoup(r.content,"html.parser")
print(soup.prettify())


browser=webdriver.Chrome()
time.sleep(2)

browser.get(content)

time.sleep(2)


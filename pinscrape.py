from selenium import webdriver
from bs4 import BeautifulSoup
import sys
import time
from random_word import RandomWords
from auto_test import move 
from auto_test import toggle
from auto_test import paste
import pyperclip as pc
import os

def defaultValue():
    r = RandomWords()
    randomValue = r.get_random_word()
    return randomValue

def searchValue(n):
    temp = []
    search_param = ""
    for x in range(n):
        temp.append(sys.argv[x] + " ")
    del temp[0]
    for x in range(len(temp)):
        search_param = search_param + temp[x]
    
    return(search_param)




def Scrape():
    os.popen("PureRef")
    browser = webdriver.Firefox()
    base = 'https://www.pinterest.com/search/pins/?q='
    n = len(sys.argv)

    if n < 2:
        search_param = defaultValue()
    else:
        search_param = searchValue(n)

    url = base + search_param
    browser.get(url)

    time.sleep(3)

    soup=BeautifulSoup(browser.page_source, features='html.parser')
    targets = []
    images = soup.findAll('img')
    for image in images:
        targets.append(image['src'])
        #pc.copy(image['src'])
    print(targets,)

    browser.quit()
    move()
    
    for image in images:
        pc.copy(image['src'])
        paste()



if __name__ == "__main__":
    Scrape()
    move()
    toggle()
    

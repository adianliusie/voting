import time
from datetime import date
import json 
from os import path

import numpy as np
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.proxy import Proxy, ProxyType

import random

def vote():
    driver = webdriver.Chrome()

    driver.get('https://bit.ly/3Jnfiuh')
    time.sleep(3)
    driver.find_element_by_id("awardVoteButton").click()
    time.sleep(3)
    driver.quit()

def vote_script():
    count = 0
    while count < 90:
        try:
           vote()
        except:
           time.sleep(2)
           vote()
        count = count+1
        print(count)

vote_script()

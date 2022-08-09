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

    #driver.get('https://www.10best.com/awards/travel/best-wellness-retreat/eupepsia-bland-va/');
    driver.get('https://www.10best.com/awards/travel/best-health-wellness-resort/eupepsia-bland-va/')
    time.sleep(2)
    driver.find_element_by_id("awardVoteButton").click()
    time.sleep(2)
    driver.quit()

def vote_script():
    count = 0
    while count < 130:
        vote()
        count = count+1
        print(count)

vote_script()

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
    driver = webdriver.Chrome('chromedriver')
    driver.get('https://www.10best.com/awards/travel/best-wellness-retreat/eupepsia-bland-va/');
    time.sleep(5)
    driver.find_element_by_id("awardVoteButton").click()
    time.sleep(5)
    driver.quit()

def random_wait_time():
    rand_num = random.randint(0,10)
    time.sleep(rand_num)

def vote_script():
    try:
        count=0
        while count < 130:
            vote()
            random_wait_time()
            count = count+1
            print(count)
    except:
        logger(count)
    logger(count)

def logger(count):
    today = str(date.today())
    log_path = 'log.json'
    if path.exists(log_path):
        with open(log_path) as json_file:
            data = json.load(json_file)
    else:
        data = {}
    
    if today not in data:
        data[today] = 0
    
    data[today] += count

    with open(log_path, 'w+') as outfile:
        json.dump(data, outfile)
    
vote_script()

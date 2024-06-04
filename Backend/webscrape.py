from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.common.keys
import random
import config
import time
import pymongo
from bson import ObjectId
from datetime import datetime

def handle_mongo(data):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    db = client["twitter"]
    collection = db['trends']
    collection.insert_one(data)
    latest_data = collection.find_one(sort=[("scrape_end_time", -1)], limit=1)
    latest_data["_id"] = str(latest_data["_id"])
    return latest_data

def rand_proxy():
    proxy = random.choice(config.ips)
    return proxy

def web_scrape():
    options = webdriver.ChromeOptions()
    proxy = rand_proxy() # Use paid proxies for better connection
    options.add_argument(f'--proxy-server={proxy}')
    options.page_load_strategy = 'normal'
    BASE_URL = 'https://x.com/home'
    browser = webdriver.Chrome(options=options) 
    browser.get(BASE_URL)

    # Login task
    try:
        popupCloseButton = WebDriverWait(browser, timeout=8).until(lambda d : d.find_element(By.XPATH, '//button[@data-testid="xMigrationBottomBar"]'))
        popupCloseButton.click()
        time.sleep(2)
        loginBtn = WebDriverWait(browser, timeout=3).until(lambda d : d.find_element(By.XPATH, '//a[@data-testid="loginButton"]'))
        loginBtn.click()
        nameField = WebDriverWait(browser, timeout=5).until(lambda d : d.find_element(By.XPATH, '//input[@name="text"]')) 
        nameField.click()
        nameField.clear()
        nameField.send_keys('gimawe1858@avastu.com')
        nextButtons = browser.find_elements(By.XPATH, '//button[@role="button"]')
        time.sleep(2)
        nextButtons[3].click()
        userName = WebDriverWait(browser, timeout=5).until(lambda d : d.find_element(By.XPATH, '//input[@type="text"]'))
        userName.click()
        userName.clear()
        userName.send_keys('ScrapeYou')
        time.sleep(1)
        userNameNextBtn =WebDriverWait(browser, timeout=3).until(lambda d : d.find_element(By.XPATH, '//button[@data-testid="ocfEnterTextNextButton"]'))
        userNameNextBtn.click()
        time.sleep(3)
        password = browser.find_element(By.XPATH, '//input[@type="password"]')
        password.click()
        password.clear()
        password.send_keys('IWILLSCRAPEYOU')
        time.sleep(2)
        passwordNextBtn = browser.find_element(By.XPATH, '//button[@data-testid="LoginForm_Login_Button"]')
        passwordNextBtn.click()
        time.sleep(1)
        trending_topics =WebDriverWait(browser, timeout=10).until(lambda d : d.find_elements(By.XPATH, '//div[@data-testid="trend"]//div[2]/span'))
    except Exception as e:
        print(e)
        return
    document = {}
    for index, topics in enumerate(trending_topics):
        print(topics.text)
        document["trend"+str(index+1)] = topics.text

    datetimenow = datetime.now()
    datetimenow = datetimenow.strftime("%Y-%m-%d %H:%M")
    document["_id"] = ObjectId()
    document["scrape_end_time"] = datetimenow
    document["ip"] = proxy

    print(document)
    latestdata = handle_mongo(document)
    print("latest")
    print(latestdata)
    time.sleep(10)
    return latestdata

web_scrape()
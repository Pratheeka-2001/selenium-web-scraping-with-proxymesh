from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium.webdriver.common.keys
import random
import config
import time

def rand_proxy():
    proxy = random.choice(config.ips)
    return proxy

def web_scrape():
    # chrome_options = webdriver.ChromeOptions()
    # proxy = rand_proxy()
    # chrome_options.add_argument(f'--proxy-server={proxy}')

    BASE_URL = 'https://x.com/home'
    # path = 'chromedriver-win64\chromedriver.exe'
    browser = webdriver.Chrome() 
    browser.get(BASE_URL)
    time.sleep(8)

    # Login task
    loginBtn = browser.find_element(By.XPATH, '//a[@data-testid="loginButton"]')
    loginBtn.click()
    time.sleep(5)
    nameField = browser.find_element(By.XPATH, '//input[@name="text"]')   
    nameField.click()
    nameField.clear()
    nameField.send_keys('gimawe1858@avastu.com')
    nextButtons = browser.find_elements(By.XPATH, '//button[@role="button"]')
    time.sleep(3)
    nextButtons[3].click()
    time.sleep(3)
    userName = browser.find_element(By.XPATH, '//input[@type="text"]')
    userName.click()
    userName.clear()
    userName.send_keys('ScrapeYou')
    time.sleep(1)
    userNameNextBtn = browser.find_element(By.XPATH, '//button[@data-testid="ocfEnterTextNextButton"]')
    userNameNextBtn.click()
    time.sleep(3)
    password = browser.find_element(By.XPATH, '//input[@type="password"]')
    password.click()
    password.clear()
    password.send_keys('IWILLSCRAPEYOU')
    time.sleep(2)
    passwordNextBtn = browser.find_element(By.XPATH, '//button[@data-testid="LoginForm_Login_Button"]')
    passwordNextBtn.click()
    time.sleep(5)
    trending_topics = browser.find_elements(By.XPATH, '//div[@data-testid="trend"]//div[2]/span') 
    for topics in trending_topics:
        print(topics.text)
    
    time.sleep(250)

if __name__ == '__main__':
    web_scrape()  
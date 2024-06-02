from selenium import webdriver
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

    BASE_URL = 'https://webscraper.io/test-sites/e-commerce/allinone'
    path = '/chromedriver-win64'
    browser = webdriver.Chrome() 
    browser.get(BASE_URL)

    browser.find_element_by_xpath('//div[@data-testid="trend"]')

    time.sleep(5)

if __name__ == '__main__':
    web_scrape()  
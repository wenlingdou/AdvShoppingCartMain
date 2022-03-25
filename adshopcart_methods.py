import datetime
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import adshopcart_locators as locators
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select  # add this import for drop down lists
from selenium.webdriver import Keys

s = Service(executable_path='../chromedriver.exe')
driver = webdriver.Chrome(service=s)

def setUp():
    print(f'*--------------------------------------------------*')
    print(f'Test start at: {datetime.datetime.now()}')

    # make browser full screen
    driver.maximize_window()
    # give browser up to 30 seconds to respond
    driver.implicitly_wait(30)

    # navigate to website
    driver.get(locators.adshopcart_url)

    # check  URL and home page title are as expected
    if driver.current_url == locators.adshopcart_url and driver.title == locators.adshopcart_homepage_title:
        print(f'{locators.app} website launched successfully!')
        print(f'{locators.app} Homepage URL: {driver.current_url}, Homepage title: {driver.title}')
        sleep(0.25)
    else:
        print(f'{locators.app} did not launch. Check your code or application!')
        print(f'Current URL: {driver.current_url}, Homepage title: {driver.title}')
        driver.close()
        driver.quit()

def tearDown():
    if driver is not None:
        print('*-----------------------------------*')
        print(f'The test is completed at: {datetime.datetime.now()}')
        sleep(0.5)
        driver.close()
        driver.quit()

# setUp()
# tearDown()
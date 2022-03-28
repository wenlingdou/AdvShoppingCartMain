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
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get(locators.adshopcart_url)

    if driver.current_url == locators.adshopcart_url and locators.adshopcart_homepage_title in driver.title:
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

def create_new_account():
    if driver.current_url == locators.adshopcart_url:
        driver.find_element(By.ID, 'menuUser').click()
        sleep(2.5)
        assert driver.find_element(By.XPATH, '//a[contains(., "CREATE NEW ACCOUNT")]')
        print('------------CREATE NEW ACCOUNT--------------')
        driver.find_element(By.XPATH, '//a[contains(., "CREATE NEW ACCOUNT")]').click()
        sleep(2.5)

def register():
    if driver.current_url == locators.adshopcart_register_url:
        print('--------------REGISTER PAGE----------')
        driver.find_element(By.NAME, 'usernameRegisterPage').send_keys(locators.username)
        sleep(0.25)
        driver.find_element(By.NAME, 'emailRegisterPage').send_keys(locators.email)
        sleep(0.25)
        driver.find_element(By.NAME, 'passwordRegisterPage').send_keys(locators.password)
        sleep(0.25)
        driver.find_element(By.NAME, 'confirm_passwordRegisterPage').send_keys(locators.password)
        sleep(0.25)
        driver.find_element(By.NAME, 'first_nameRegisterPage').send_keys(locators.firstname)
        sleep(0.25)
        driver.find_element(By.NAME, 'last_nameRegisterPage').send_keys(locators.lastname)
        sleep(0.25)
        driver.find_element(By.NAME, 'phone_numberRegisterPage').send_keys(locators.phonenum)
        sleep(0.25)
        driver.find_element(By.NAME, 'countryListboxRegisterPage').send_keys(locators.country)
        sleep(0.25)
        driver.find_element(By.NAME, 'cityRegisterPage').send_keys(locators.city)
        sleep(0.25)
        driver.find_element(By.NAME, 'addressRegisterPage').send_keys(locators.address)
        sleep(0.25)
        driver.find_element(By.NAME, 'state_/_province_/_regionRegisterPage').send_keys(locators.province)
        sleep(0.25)
        driver.find_element(By.NAME, 'postal_codeRegisterPage').send_keys(locators.postalcode)
        sleep(0.25)
        driver.find_element(By.NAME, 'i_agree').click()
        sleep(0.5)
        driver.find_element(By.ID, 'register_btnundefined').click()
        sleep(1.5)

def check_fullname():
    if driver.current_url == locators.adshopcart_url:
        print('------------CHECK FULL NAME--------------')
        driver.find_element(By.ID, 'menuUser').click()
        sleep(0.5)
        print(f'--------Username: {locators.username}------')
        driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[1]').click()
        sleep(0.5)
    if driver.current_url == locators.adshopcart_account_url:
        print('-------------MY ACCOUNT PAGE---------')
        assert driver.find_element(By.XPATH, f'//label[contains(., "{locators.fullname}")]').is_displayed()
        sleep(0.5)
        print(f'----------Fullname: {locators.fullname}--------')

def check_orders():
    driver.find_element(By.ID, 'menuUser').click()
    sleep(0.5)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[2]').click()
    sleep(0.5)
    if driver.current_url == locators.adshopcart_orders_url:
        print('----------CHECK ORDERS---------------')
    assert driver.find_element(By.XPATH, '/html/body/div[3]/section/article/div[3]/div/div/label').is_displayed()
    sleep(0.25)
    print('---------No orders---------')

def logout():
    driver.find_element(By.ID, 'menuUser').click()
    sleep(0.5)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[3]').click()
    sleep(0.5)
    print('---------------SIGN OUT--------------')

def login():
    if driver.current_url == locators.adshopcart_url:
        print('---------LOGIN----------')
        driver.find_element(By.ID, 'menuUser').click()
        sleep(2.5)
        driver.find_element(By.NAME, 'username').send_keys(locators.username)
        sleep(0.25)
        driver.find_element(By.NAME, 'password').send_keys(locators.password)
        sleep(0.25)
        driver.find_element(By.ID, 'sign_in_btnundefined').click()
        sleep(0.5)

def delete_account():
    driver.find_element(By.ID, 'menuUser').click()
    sleep(0.5)
    print(f'--------Username: {locators.username}------')
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[1]').click()
    sleep(1.5)
    driver.find_element(By.CLASS_NAME, 'deleteBtnText').click()
    sleep(1.5)
    print('----------DELETE ACCOUNT------------')
    driver.find_element(By.XPATH, '//*[@id="deleteAccountPopup"]/div[3]/div[1]').click()
    sleep(5)

# validate deletion new user
def check_delete():
    if driver.find_element(By.XPATH, '//label[contains(., "Incorrect user name or password.")]').is_displayed():
        sleep(0.5)
        print(f'Incorrect user name or password. Username: {locators.username} was not exsiting.')
    else:
        print('Something went wrong. Please check your code.')


# setUp()
# create_new_account()
# register()
# check_fullname()
# check_orders()
# logout()
# login()
# delete_account()
# login()
# check_delete()
# tearDown()
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def login_page():
    browser = webdriver.Chrome(executable_path=r"C:\Users\User\Downloads\chromedriver-win64\chromedriver.exe")
    browser.maximize_window()
    browser.get("https://parabank.parasoft.com/")
    time.sleep(3)
    browser.find_element(By.XPATH, "//input[@name='username']").send_keys("john")
    time.sleep(3)
    browser.find_element(By.XPATH, "//input[@name='password']").send_keys("demo")
    time.sleep(3)
    browser.find_element(By.XPATH, "//input[@value='Log In']").click()
    browser.save_screenshot("C:\\Users\\User\\Desktop\\Practice\\ParaBank\\Screenshots\\login_screen.png")

    yield browser

    time.sleep(5)
    browser.find_element(By.XPATH, "//a[normalize-space()='Log Out']").click()
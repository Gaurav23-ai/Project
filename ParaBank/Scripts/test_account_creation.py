import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Scripts.conftest import login_page


def test_account_opening(login_page):
    driver = login_page
    time.sleep(3)
    driver.find_element(By.XPATH, value="//a[normalize-space()='Open New Account']").click()
    driver.find_element(By.XPATH, value="(//select[@id='type'])[1]").click()
    time.sleep(3)
    drop_down = driver.find_element(By.XPATH, value="(//select[@id='type'])[1]")
    dd = Select(drop_down)
    dd.select_by_value("1")
    time.sleep(2)
    driver.find_element(By.XPATH, value="//input[@value='Open New Account']").click()
    time.sleep(2)
    driver.save_screenshot("C:\\Users\\User\\Desktop\\Practice\\ParaBank\\Screenshots\\account_opening.png")


def test_account_overview(login_page):
    driver = login_page
    time.sleep(3)
    driver.find_element(By.XPATH, value="(//a[normalize-space()='Accounts Overview'])[1]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, value="//a[normalize-space()='13344']").click()
    time.sleep(5)
    driver.find_element(By.XPATH, value="//input[@value='Go']").click()
    time.sleep(4)
    driver.save_screenshot("C:\\Users\\User\\Desktop\\Practice\\ParaBank\\Screenshots\\account_overview.png")

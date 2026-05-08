from selenium.webdriver.common.by import By

from eapp.test.pages.HomePage import HomePage
from eapp.test.test_base import driver, test_app
import time

def test_search_products(driver):
    # driver.get('http://127.0.0.1:5000/')
    # e = driver.find_element(By.CSS_SELECTOR, '#collapsibleNavbar > form > input')
    kw = 'iPhone'
    # e.send_keys(kw)
    # driver.find_element(By.CSS_SELECTOR, '#collapsibleNavbar > form > button').click()
    home = HomePage(driver=driver)
    home.open_page()
    home.search(kw)

    time.sleep(1)

    results = driver.find_elements(By.CSS_SELECTOR, '.container .card-title')
    assert all (kw in r.text for r in results)

def test_order(driver):
    home = HomePage(driver=driver)
    home.open_page()
    home.order()

    e = driver.find_element(By.CLASS_NAME, 'cart-counter')
    assert int(e.text) == 3
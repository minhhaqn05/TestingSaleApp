from selenium.webdriver.common.by import By

from eapp.test.pages.BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC


class CartPage(BasePage):
    URL = 'http://127.0.0.1:5000/cart'

    PAY_BUTTON = (By.CSS_SELECTOR, 'body > section > div.mt-1.mb-1 > button')
    INPUT_ITEM1 = (By.CSS_SELECTOR, 'tbody > tr > td:nth-child(4) > input')
    BODY = (By.TAG_NAME, 'body')

    def open_page(self):
        self.open(self.URL)

    def pay(self):
        self.click(*self.PAY_BUTTON)

        wait = WebDriverWait(self.driver, 10)
        alert = wait.until(EC.alert_is_present())

        alert.accept()

    def update_cart_item(self, num):
        e = self.find(*self.INPUT_ITEM1)
        e.clear()
        e.send_keys(num)

        self.click(*self.BODY)

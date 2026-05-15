from selenium.webdriver.common.by import By

from eapp.test.pages.BasePage import BasePage


class RegisterPage(BasePage):
    URL = 'http://127.0.0.1:5000/register'

    NAME = (By.ID, 'name')
    USERNAME = (By.ID, 'username')
    PASSWORD = (By.ID, 'pwd')
    CONFIRM = (By.ID, 'confirm')
    AVATAR = (By.ID, 'avatar')
    BUTTON = (By.CSS_SELECTOR, 'body > section > form > div:nth-child(6) > button')

    def open_page(self):
        self.open(self.URL)

    def register(self, name, username, password, confirm, avatar):
        self.typing(*self.NAME, name)
        self.typing(*self.USERNAME, username)
        self.typing(*self.PASSWORD, password)
        self.typing(*self.CONFIRM, confirm)
        self.typing(*self.AVATAR, avatar)
        self.click(*self.BUTTON)

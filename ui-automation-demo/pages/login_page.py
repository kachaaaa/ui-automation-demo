from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    def login(self, username, password):
        self.type(*self.USERNAME, username)
        self.type(*self.PASSWORD, password)
        self.click(*self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.find(*self.ERROR_MESSAGE).text

    from selenium.webdriver.common.by import By

    class LoginPage:
        ...

        success_message = (By.CSS_SELECTOR, "h2")

        def is_login_successful(self):
            return "Secure Area" in self.driver.find_element(*self.success_message).text
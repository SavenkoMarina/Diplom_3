from allure import step

from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from locators.recover_page_locators import RecoverPageLocators
from data import urls

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.go_to_url(urls.LOGIN_URL)
        self.wait_for_clickable_element(LoginPageLocators.RECOVER_LINK)

    @step("Открыть восстановление пароля")
    def open_password_recovery(self):
        self.click_element(LoginPageLocators.RECOVER_LINK)
        self.wait_for_load_element(RecoverPageLocators.RECOVER_BTN)
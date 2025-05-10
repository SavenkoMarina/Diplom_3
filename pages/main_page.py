from allure import step

from locators.account_page_locators import AccountPageLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from data import urls

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.go_to_url(urls.MAIN_URL)
        self.wait_for_clickable_element(MainPageLocators.ROOT_FIELD)

    @step("Перейти в личный кабинет")
    def click_to_account(self):
        self.wait_for_clickable_element(MainPageLocators.ACCOUNT_LINK)
        self.click_element(MainPageLocators.ACCOUNT_LINK)
        self.wait_for_load_element(AccountPageLocators.LOGOUT_LINK)


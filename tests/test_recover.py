from allure import title
from data import urls
from locators.reset_page_locators import ResetPageLocators
from pages.login_page import LoginPage
from pages.recover_page import RecoverPage
from pages.reset_page import ResetPage
from helpers import generate_email


class TestRecoverPage:

    @title("Переход на страницу восстановления пароля")
    def test_recover_link(self, driver):
        page = LoginPage(driver)
        page.open_password_recovery()
        assert driver.current_url == urls.RECOVER_URL

    @title("Ввод почты и клик по кнопке «Восстановить»")
    def test_request_password_recover(self, driver):
        page = RecoverPage(driver)

        email = generate_email()
        page.enter_email(email)
        page.click_to_recover()

        assert driver.current_url == urls.RESET_URL

    @title("Показать/скрыть пароль")
    def test_show_password(self, driver):
        page = ResetPage(driver)

        page.enter_password("test")
        page.click_show_password()

        pwd_input = page.find_element(ResetPageLocators.PASSWORD_INPUT_PARENT)

        assert "input_status_active" in pwd_input.get_attribute("class")

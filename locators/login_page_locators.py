from selenium.webdriver.common.by import By


class LoginPageLocators:
    RECOVER_LINK = (By.XPATH, "//a[@href='/forgot-password']")
from selenium.webdriver.common.by import By


class MainPageLocators:
    ROOT_FIELD = (By.ID, "root")
    FIRST_BUN_LINK = (By.XPATH, "//div[@class='BurgerIngredients_ingredients__menuContainer__Xu3Mo']/ul[1]/a[1]")
    ACCOUNT_LINK = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")

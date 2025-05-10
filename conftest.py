import pytest
from selenium import webdriver
from api import API
from helpers import generate_random_string


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def user():
    email = f"{generate_random_string(5)}@ya.ru"
    password = f"{generate_random_string(8)}"
    name = f"{generate_random_string(10)}"

    api = API()
    api.register_user(email, password, name)
    yield {
        "email": email,
        "password": password,
        "name": name,
    }

    api.login_user(email, password)
    api.delete_user()

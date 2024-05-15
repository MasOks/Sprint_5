import pytest
from selenium import webdriver
from config import URL, NAME, EMAIL, PASSWORD
from locators import StellarLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


@pytest.fixture
def driver1():
    chrome = webdriver.Chrome()
    chrome.get(URL)
    yield chrome
    chrome.quit()


@pytest.fixture
def driver2():
    firefox = webdriver.Firefox()
    firefox.get(URL)
    yield firefox
    firefox.quit()


@pytest.fixture
def registration_on_stellar(driver1):
    driver1.get(f'{URL}register')
    driver1.find_element(*StellarLocators.NAME_FIELD_REG).send_keys(NAME)
    driver1.find_element(*StellarLocators.EMAIL_FIELD_REG).send_keys(EMAIL)
    driver1.find_element(*StellarLocators.PASSWORD_FIELD_REG).send_keys(PASSWORD)
    driver1.find_element(*StellarLocators.BUTTON_REGISTRATION).click()
    WebDriverWait(driver1, 10).until(
        expected_conditions.visibility_of_element_located(StellarLocators.PAGE_INPUT))

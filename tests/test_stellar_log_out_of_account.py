import random


from locators import StellarLocators
from config import URL
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestStellarLogOutOfAccount:

    def test_log_out_of_account_using_button_in_account_in_chrome(self, driver1):
        new_name = f'OksanaMasyarkina8{random.randint(100, 999)}'
        new_email = f'{new_name}@yandex.ru'
        driver1.get(f'{URL}register')
        driver1.find_element(*StellarLocators.NAME_FIELD_REG).send_keys(new_name)
        driver1.find_element(*StellarLocators.EMAIL_FIELD_REG).send_keys(new_email)
        driver1.find_element(*StellarLocators.PASSWORD_FIELD_REG).send_keys("123456789test")
        driver1.find_element(*StellarLocators.BUTTON_REGISTRATION).click()
        WebDriverWait(driver1, 10).until(
            expected_conditions.visibility_of_element_located(StellarLocators.PAGE_INPUT))
        driver1.get(f'{URL}login')
        driver1.find_element(*StellarLocators.EMAIL_FIELD_IN).send_keys(new_email)
        driver1.find_element(*StellarLocators.PASSWORD_FIELD_IN).send_keys("123456789test")
        driver1.find_element(*StellarLocators.BUTTON_ENTER_IN).click()
        WebDriverWait(driver1, 10).until(
            expected_conditions.visibility_of_element_located(StellarLocators.BUTTON_PLACE_AN_ORDER))

        driver1.find_element(*StellarLocators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver1, 10).until(
            expected_conditions.visibility_of_element_located(StellarLocators.BUTTON_OUTPUT))
        driver1.find_element(*StellarLocators.BUTTON_OUTPUT).click()
        WebDriverWait(driver1, 10).until(
            expected_conditions.visibility_of_element_located(StellarLocators.PAGE_INPUT))
        page_input = driver1.find_element(*StellarLocators.PAGE_INPUT)
        assert page_input.is_displayed()

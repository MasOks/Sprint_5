from locators import StellarLocators
from config import URL, NAME, EMAIL, PASSWORD
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestStellarRegistration:

    def test_successful_registration_in_chrome(self, driver1):
        driver1.get(f'{URL}register')
        driver1.find_element(*StellarLocators.NAME_FIELD_REG).send_keys(NAME)
        driver1.find_element(*StellarLocators.EMAIL_FIELD_REG).send_keys(EMAIL)
        driver1.find_element(*StellarLocators.PASSWORD_FIELD_REG).send_keys(PASSWORD)
        driver1.find_element(*StellarLocators.BUTTON_REGISTRATION).click()
        WebDriverWait(driver1, 10).until(
            expected_conditions.visibility_of_element_located(StellarLocators.PAGE_INPUT))
        driver1.get(f'{URL}login')
        driver1.find_element(*StellarLocators.EMAIL_FIELD_IN).send_keys(EMAIL)
        driver1.find_element(*StellarLocators.PASSWORD_FIELD_IN).send_keys(PASSWORD)
        driver1.find_element(*StellarLocators.BUTTON_ENTER_IN).click()
        WebDriverWait(driver1, 10).until(
            expected_conditions.visibility_of_element_located(StellarLocators.BUTTON_PLACE_AN_ORDER))
        button_place_an_order = driver1.find_element(*StellarLocators.BUTTON_PLACE_AN_ORDER)
        assert button_place_an_order.is_displayed()

    def test_successful_registration_in_firefox(self, driver2):
        driver2.get(f'{URL}register')
        driver2.find_element(*StellarLocators.NAME_FIELD_REG).send_keys(NAME)
        driver2.find_element(*StellarLocators.EMAIL_FIELD_REG).send_keys(EMAIL)
        driver2.find_element(*StellarLocators.PASSWORD_FIELD_REG).send_keys(PASSWORD)
        driver2.find_element(*StellarLocators.BUTTON_REGISTRATION).click()
        WebDriverWait(driver2, 10).until(
            expected_conditions.visibility_of_element_located(StellarLocators.PAGE_INPUT))
        driver2.get(f'{URL}login')
        driver2.find_element(*StellarLocators.EMAIL_FIELD_IN).send_keys(EMAIL)
        driver2.find_element(*StellarLocators.PASSWORD_FIELD_IN).send_keys(PASSWORD)
        driver2.find_element(*StellarLocators.BUTTON_ENTER_IN).click()
        WebDriverWait(driver2, 10).until(
            expected_conditions.visibility_of_element_located(StellarLocators.BUTTON_PLACE_AN_ORDER))
        button_place_an_order = driver2.find_element(*StellarLocators.BUTTON_PLACE_AN_ORDER)
        assert button_place_an_order.is_displayed()

    def test_invalid_password_for_registration_in_chrome(self, driver1):
        driver1.get(f'{URL}register')
        driver1.find_element(*StellarLocators.NAME_FIELD_REG).send_keys(NAME)
        driver1.find_element(*StellarLocators.EMAIL_FIELD_REG).send_keys(EMAIL)
        driver1.find_element(*StellarLocators.PASSWORD_FIELD_REG).send_keys("1test")
        driver1.find_element(*StellarLocators.BUTTON_REGISTRATION).click()
        WebDriverWait(driver1, 10).until(
            expected_conditions.visibility_of_element_located(StellarLocators.INVALID_PASSWORD))
        invalid_password = driver1.find_element(*StellarLocators.INVALID_PASSWORD)
        assert invalid_password.is_displayed()

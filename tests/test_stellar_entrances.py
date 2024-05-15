from locators import StellarLocators
from config import URL, EMAIL, PASSWORD
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestStellarEntrances:

    def test_enter_by_button_log_in_to_account_in_chrome(self, driver1, registration_on_stellar):
        driver1.get(URL)
        driver1.find_element(*StellarLocators.BUTTON_LOG_IN_TO_ACCOUNT).click()
        WebDriverWait(driver1, 10).until(
            expected_conditions.visibility_of_element_located(StellarLocators.PAGE_INPUT))
        driver1.find_element(*StellarLocators.EMAIL_FIELD_IN).send_keys(EMAIL)
        driver1.find_element(*StellarLocators.PASSWORD_FIELD_IN).send_keys(PASSWORD)
        driver1.find_element(*StellarLocators.BUTTON_ENTER_IN).click()
        WebDriverWait(driver1, 10).until(
            expected_conditions.visibility_of_element_located(StellarLocators.BUTTON_PLACE_AN_ORDER))
        button_place_an_order = driver1.find_element(*StellarLocators.BUTTON_PLACE_AN_ORDER)
        assert button_place_an_order.is_displayed()

    def test_enter_by_button_personal_account_in_chrome(self, driver1, registration_on_stellar):
        driver1.get(f'{URL}login')
        driver1.find_element(*StellarLocators.EMAIL_FIELD_IN).send_keys(EMAIL)
        driver1.find_element(*StellarLocators.PASSWORD_FIELD_IN).send_keys(PASSWORD)
        driver1.find_element(*StellarLocators.BUTTON_ENTER_IN).click()
        WebDriverWait(driver1, 10).until(
            expected_conditions.visibility_of_element_located(StellarLocators.BUTTON_PLACE_AN_ORDER))
        driver1.find_element(*StellarLocators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver1, 10).until(
            expected_conditions.visibility_of_element_located(StellarLocators.BUTTON_SAVE))
        button_save = driver1.find_element(*StellarLocators.BUTTON_SAVE)
        assert button_save.is_displayed()

    def test_enter_by_button_in_form_of_registration_in_chrome(self, driver1, registration_on_stellar):
        driver1.get(f'{URL}register')
        driver1.find_element(*StellarLocators.BUTTON_ENTER).click()
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

    def test_enter_by_button_in_form_of_password_recovery_in_chrome(self, driver1, registration_on_stellar):
        driver1.get(f'{URL}login')
        driver1.find_element(*StellarLocators.BUTTON_PASSWORD_RECOVERY).click()
        WebDriverWait(driver1, 10).until(
            expected_conditions.visibility_of_element_located(StellarLocators.BUTTON_RECOVER))
        driver1.get(f'{URL}forgot-password')
        driver1.find_element(*StellarLocators.BUTTON_ENTER).click()
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

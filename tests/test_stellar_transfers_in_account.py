from locators import StellarLocators
from config import URL, EMAIL, PASSWORD
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestStellarTransfersInAccount:

    def test_transfer_in_to_account_before_log_in_in_chrome(self, driver1, registration_on_stellar):
        driver1.get(URL)
        driver1.find_element(*StellarLocators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver1, 10).until(
            expected_conditions.visibility_of_element_located(StellarLocators.PAGE_INPUT))
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

    def test_transfer_in_to_account_after_log_in_in_chrome(self, driver1, registration_on_stellar):
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

    def test_transfer_from_account_to_constructor_in_chrome(self, driver1, registration_on_stellar):
        driver1.get(f'{URL}login')
        driver1.find_element(*StellarLocators.EMAIL_FIELD_IN).send_keys(EMAIL)
        driver1.find_element(*StellarLocators.PASSWORD_FIELD_IN).send_keys(PASSWORD)
        driver1.find_element(*StellarLocators.BUTTON_ENTER_IN).click()
        WebDriverWait(driver1, 10).until(
            expected_conditions.visibility_of_element_located(StellarLocators.BUTTON_PLACE_AN_ORDER))
        driver1.find_element(*StellarLocators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver1, 10).until(
            expected_conditions.visibility_of_element_located(StellarLocators.BUTTON_SAVE))
        driver1.find_element(*StellarLocators.BUTTON_CONSTRUCTOR).click()
        WebDriverWait(driver1, 10).until(
            expected_conditions.visibility_of_element_located(StellarLocators.BUTTON_PLACE_AN_ORDER))
        button_place_an_order = driver1.find_element(*StellarLocators.BUTTON_PLACE_AN_ORDER)
        assert button_place_an_order.is_displayed()

    def test_transfer_from_account_to_logo_in_chrome(self, driver1, registration_on_stellar):
        driver1.get(f'{URL}login')
        driver1.find_element(*StellarLocators.EMAIL_FIELD_IN).send_keys(EMAIL)
        driver1.find_element(*StellarLocators.PASSWORD_FIELD_IN).send_keys(PASSWORD)
        driver1.find_element(*StellarLocators.BUTTON_ENTER_IN).click()
        WebDriverWait(driver1, 10).until(
            expected_conditions.visibility_of_element_located(StellarLocators.BUTTON_PLACE_AN_ORDER))
        driver1.find_element(*StellarLocators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver1, 10).until(
            expected_conditions.visibility_of_element_located(StellarLocators.BUTTON_SAVE))
        driver1.find_element(*StellarLocators.BUTTON_LOGO).click()
        WebDriverWait(driver1, 10).until(
            expected_conditions.visibility_of_element_located(StellarLocators.BUTTON_PLACE_AN_ORDER))
        button_place_an_order = driver1.find_element(*StellarLocators.BUTTON_PLACE_AN_ORDER)
        assert button_place_an_order.is_displayed()

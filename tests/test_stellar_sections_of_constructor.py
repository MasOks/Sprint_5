from locators import StellarLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestStellarSectionsOfConstructor:

    def test_go_to_the_fillings_section_in_constructor_in_chrome(self, driver1):
        driver1.find_element(*StellarLocators.SECTION_FILLINGS).click()
        WebDriverWait(driver1, 5).until(
            expected_conditions.visibility_of_element_located(StellarLocators.LIST_FILLINGS))
        list_fillings = driver1.find_element(*StellarLocators.LIST_FILLINGS)
        assert list_fillings.is_displayed()

    def test_go_to_the_sauces_section_in_constructor_in_chrome(self, driver1):
        driver1.find_element(*StellarLocators.SECTION_SAUCES).click()
        WebDriverWait(driver1, 5).until(
            expected_conditions.visibility_of_element_located(StellarLocators.LIST_SAUCES))
        list_sauces = driver1.find_element(*StellarLocators.LIST_SAUCES)
        assert list_sauces.is_displayed()

    def test_go_to_the_bread_section_in_constructor_in_chrome(self, driver1):
        driver1.find_element(*StellarLocators.SECTION_FILLINGS).click()
        WebDriverWait(driver1, 5).until(
            expected_conditions.visibility_of_element_located(StellarLocators.LIST_FILLINGS))
        driver1.find_element(*StellarLocators.SECTION_BREAD).click()
        WebDriverWait(driver1, 5).until(
            expected_conditions.visibility_of_element_located(StellarLocators.LIST_BREAD))
        list_bread = driver1.find_element(*StellarLocators.LIST_BREAD)
        assert list_bread.is_displayed()

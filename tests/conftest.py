import pytest
from selenium import webdriver
from config import URL


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

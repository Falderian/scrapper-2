from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def waitCheckHtmlExisting(browser, selector, text):
    return WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((selector, text))
    )

import constants as CONST
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WebDriver:
    def __init__(self):
        self.path = CONST.CHROME_DRIVER_PATH
        self.newsletterPageUrl = CONST.ZALANDO_URL
        self.emailGeneratorUrl = CONST.EMAIL_GENERATOR_URL
        self.driver = None

    def get_driver(self):
        if self.driver is None:
            options = Options()
            options.headless = False  # set True to use Chrome in headless mode
            self.driver = webdriver.Chrome(options=options, executable_path=self.path)
        return self.driver

    def try_get_element(self, timeout, method, properties):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((method, properties))
            )
            if element is not None:
                return element
        except:
            self.try_get_element(timeout, method, properties)

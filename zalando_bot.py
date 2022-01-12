import constants as CONST
import datetime
from selenium.webdriver.common.by import By
from web_driver import WebDriver


class ZalandoBot:
    def __init__(self, timeout):
        self.timeout = timeout

    def log(self, message, severity):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f"[{current_time}] - {severity} - {message}")

    def generate_code(self) -> str:
        try:
            web_driver = WebDriver()
            bot_driver = web_driver.get_driver()

            # create email
            bot_driver.get(CONST.EMAIL_GENERATOR_URL)
            email = bot_driver.find_element(By.ID, CONST.EMAIL_FROM_GENERATOR_ID).text
            emailGeneratorUrl = CONST.EMAIL_GENERATOR_URL + email

            # go to zalando page
            bot_driver.execute_script("window.open('about:blank','tab2');")
            bot_driver.switch_to.window('tab2')
            bot_driver.get(CONST.ZALANDO_URL)

            # ## cookie consent - can be omitted I guess?
            # cookie_btn = bot_driver.find_element(By.ID, CONST.ZALANDO_COOKIE_CONSENT_ID)
            # cookie_btn.click()

            ## set email
            email_input = web_driver.try_get_element(5, By.ID, CONST.ZALANDO_EMAIL_INPUT_FIELD_ID)
            email_input.send_keys(email)

            ## fill preferences
            preferences_btn = web_driver.try_get_element(5, By.XPATH, CONST.ZALANDO_PREFERENCES_XPATH)
            preferences_btn.click()

            ## confirm newsletter email
            subscribe_button = bot_driver.find_element(By.XPATH, CONST.ZALANDO_SUBSCRIBE_BUTTON_XPATH)
            subscribe_button.click()

            # go to email generator
            bot_driver.switch_to.window(bot_driver.window_handles[0])

            ## open email with confirmation btn
            email_with_confirmation = web_driver.try_get_element(10, By.XPATH, CONST.EMAIL_SUBSCRIBE_BUTTON_XPATH)
            email_with_confirmation.click()

            # go to email generator
            bot_driver.switch_to.window(bot_driver.window_handles[0])
            bot_driver.refresh()

            ## open email with code
            email = web_driver.try_get_element(10, By.XPATH, CONST.EMAIL_WITH_CODE_XPATH)
            email.click()

            ## get code from email
            code = web_driver.try_get_element(2, By.XPATH, CONST.EMAIL_CODE_XPATH)
            return code.text

        except Exception as e:
            return e

    def submit_newsletter_request(self, email):
        while True:
            try:
                print('Accepting cookies')
                self.driver.find_element(By.ID, CONST.ZALANDO_COOKIE_CONSENT_ID).click()
                break
            except:
                pass
        while True:
            try:
                print('Typing email')
                self.driver.find_element(By.ID, CONST.ZALANDO_EMAIL_INPUT_FIELD_ID).send_keys(email)
                break
            except:
                pass
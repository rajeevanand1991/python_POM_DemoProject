from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage

class HomePage(BasePage):

    HEADER = (By.CSS_SELECTOR, "h1.dashboard-selector__title")
    ACCOUNT_NAME = (By.CSS_SELECTOR, "span.account-name")
    SETTINGS_ICON = (By.ID, "navSetting")

    def __init__(self, driver):
        super().__init__(driver)

    def get_home_page_title(self, title):
        return self.get_title(title)

    def is_settings_icon_exist(self):
        return self.is_visible(self.SETTINGS_ICON)

    def get_header_value(self):
        if self.is_visible(self.HEADER):
            return self.get_element_text(self.HEADER)

    def get_account_name_value(self):
        if self.is_visible(self.ACCOUNT_NAME):
            return self.get_element_text(self.ACCOUNT_NAME)
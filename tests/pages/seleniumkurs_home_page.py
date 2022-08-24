from selenium.webdriver.common.by import By


class SeleniumKursHomePage:

    STATUS_MELDUNG = (By.CSS_SELECTOR, "div.portalMessage:nth-child(1)")
    BTN_HAUPTMENU = (By.ID, "portaltab-burger-menu")
    LINK_SELENIUMTESTAPP = (By.LINK_TEXT, "Selenium Testapplikationen")


    def __init__(self, driver):
        self.driver =driver

    def statusmeldung_auslesen(self):
        return self.driver.find_element(*self.STATUS_MELDUNG).text

    def hauptmenu_aufrufen(self):
        self.driver.find_element(*self.BTN_HAUPTMENU).click()

    def selenium_test_app_anklicken(self):
        self.driver.find_element(*self.LINK_SELENIUMTESTAPP).click()

        

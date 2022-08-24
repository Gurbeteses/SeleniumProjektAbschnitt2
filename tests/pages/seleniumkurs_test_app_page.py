from selenium.webdriver.common.by import By


class SeleniumKursTestAppPage:

    BTN_HAUPTMENU = (By.ID, "portaltab-burger-menu")
    LINK_TESTFORM1 = (By.LINK_TEXT, "Selenium Test Form1")


    def hauptmenu_aufrufen(self):
        self.driver.find_element(*self.BTN_HAUPTMENU).click()

    def test_form1_anklicken(self):
        self.driver.find_element(*self.LINK_TESTFORM1).click()



    def __init__(self, driver):
        self.driver = driver

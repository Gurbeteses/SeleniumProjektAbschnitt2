import unittest


from selenium import webdriver
from selenium.webdriver.common.by import By

from tests.pages.seleniumkurs_home_page import SeleniumKursHomePage
from tests.pages.seleniumkurs_login_page import SeleniumKursLoginPage
from tests.pages.seleniumkurs_test_app_page import SeleniumKursTestAppPage
from tests.pages.seleniumkurs_testform1_page import SeleniumKursTestForm1Page


class TestLoginSeleniumKursFireFox(unittest.TestCase):

    def setUp(self):
        print("Initialisiere WebDriver für den Test")
        self.driver = webdriver.Firefox()
        self.driver.get("https://seleniumkurs.codingsolo.de")

    def tearDown(self):
        print("Nach dem Test. Ich räume auf")
        self.driver.close()

    def test_login(self):
        print("Starte test_login")

        ##Arrange

        loginPage = SeleniumKursLoginPage(self.driver)
        loginPage.zugangsdaten_eingeben("selenium42", "R5vxI0j60")
        loginPage.login_button_anklicken()

        ##Act

        homePage = SeleniumKursHomePage(self.driver)
        homePage.hauptmenu_aufrufen()
        homePage.selenium_test_app_anklicken()

        testAppPage = SeleniumKursTestAppPage(self.driver)
        testAppPage.test_form1_anklicken()



        # Assert

        testForm1Page = SeleniumKursTestForm1Page(self.driver)
        erfolgsmeldung = testForm1Page.ueberschrift_auslesen()
        self.assertEqual(erfolgsmeldung,"Selenium Test Form1")

    if __name__=='__main__':
        unittest.main()
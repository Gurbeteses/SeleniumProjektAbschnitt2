import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

from tests.pages.seleniumkurs_login_page import SeleniumKursLoginPage


class TestLoginSeleniumKursFireFox(unittest.TestCase):

    def setUp(self):
        print("Initialisiere WebDriver für den Test")
        self.driver = webdriver.Firefox()
        self.driver.get("https://seleniumkurs.codingsolo.de")

    def tearDown(self):
        print("Nach dem Test. Ich räume auf")
        #self.driver.close()

    def test_login(self):
        print("Starte test_login")


        ##Arrange

        loginPage = SeleniumKursLoginPage(self.driver)
        loginPage.zugangsdaten_eingeben("selenium42", "R5vxI0j60")

        ##Act

        loginPage.login_button_anklicken()

        #Assert

        erfolgsmeldung = loginPage.statusmeldung_auslesen()
        self.assertTrue('Willkommen' in erfolgsmeldung)



    if __name__=='__main__':
        unittest.main()

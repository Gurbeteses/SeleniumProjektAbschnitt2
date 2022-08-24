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
        self.driver.close()

    def test_login(self):
        print("Starte test_login")

        ##Arrange

        loginPage = SeleniumKursLoginPage(self.driver)
        loginPage.zugangsdaten_eingeben("Benutzer", "Test")

        ##Act

        loginPage.login_button_anklicken()

        # Assert

        fehlermeldung = loginPage.statusmeldung_auslesen()
        self.assertTrue('Anmeldung fehlgeschlagen' in fehlermeldung)


    if __name__=='__main__':
        unittest.main()

import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class TestLoginSeleniumKursFireFox(unittest.TestCase):

    def setUp(self):
        print("Initialisiere WebDriver für den Test")
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://seleniumkurs.codingsolo.de")

    def tearDown(self):
        print("Nach dem Test. Ich räume auf")
        self.driver.close()

    def test_login(self):
        print("Starte test_login")


        ##Arrange

        #Login

        inputUsername = self.driver.find_element(By.CSS_SELECTOR, value="input.form-control[type='text']")
        inputUsername.send_keys("selenium42")

        inputPassword = self.driver.find_element(By.CSS_SELECTOR, value="input.form-control[type='password']")
        inputPassword.send_keys("R5vxI0j60")

        buttonLogin = self.driver.find_element(By.CSS_SELECTOR, value="input[value='Anmelden']")
        buttonLogin.click()

        #Navigation durch das Portal

        buttonMenu = self.driver.find_element(By.ID, value="portaltab-burger-menu")
        buttonMenu.click()

        linkSideNavi = self.driver.find_element(By.CSS_SELECTOR, value="a[title='Selenium Testapplikationen'] span[class='menu-item-title']")
        linkSideNavi.click()

        linkSeleniumApp = self.driver.find_element(By.LINK_TEXT, value="Selenium Test Form1")
        linkSeleniumApp.click()

        #Starte Formular

        inputBetreff = self.driver.find_element(By.ID, value="form-widgets-betreff")
        inputBetreff.send_keys("Automatischer Test")

        inputName = self.driver.find_element(By.ID, value="form-widgets-name")
        inputName.send_keys("Dieter")

        selectAuswahl1 = Select(self.driver.find_element(By.ID, value="form-widgets-auswahl1"))
        selectAuswahl1.select_by_visible_text("Java Grundlagen Kurs mit Dieter")

        selectAuswahl2 = Select(self.driver.find_element(By.ID, value="form-widgets-auswahl2-from"))

        selectAuswahl2.select_by_index("2")
        selectAuswahl2.select_by_index("4")
        selectAuswahl2.select_by_index("6")

        self.driver.find_element(By.NAME, value="from2toButton").click()

        selectAuswahl3 = Select(self.driver.find_element(By.ID, value="form-widgets-auswahl2-to"))
        selectAuswahl3.select_by_index(2)

        buttonUp = self.driver.find_element(By.NAME, value="upButton")
        buttonUp.click()

        #Act

        buttonSave = self.driver.find_element(By.NAME, value="form.buttons.speichern")
        buttonSave.click()

        #Assert


        vergleich = self.driver.find_element(By.ID, value="message").text
        self.assertTrue('Java Grundlagen Kurs' in vergleich)

        #erstesElement = self.driver.find_element(By.XPATH, value="//ul[@id='companies']/li[1]")
        #self.assertEqual(erstesElement, "Volkswagen")

    if __name__=='__main__':
        unittest.main()

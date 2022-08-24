import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class TestElementeRadioButtonSeleniumKursFireFox(unittest.TestCase):

    def setUp(self):
        print("Initialisiere WebDriver für den Test")
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://seleniumkurs.codingsolo.de")

    def tearDown(self):
        print("Nach dem Test. Ich räume auf")
        self.driver.close()

    def test_radio_button(self):
        print("Starte test_radio_button")


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

        linkSeleniumApp = self.driver.find_element(By.LINK_TEXT, value="Web Elemente")
        linkSeleniumApp.click()

        #Starte Radio Button

        radiobutton1 = self.driver.find_element(By.CSS_SELECTOR, value="input[value='radio1']")
        radiobutton2 = self.driver.find_element(By.CSS_SELECTOR, value="input[value='radio2']")
        radiobutton3 = self.driver.find_element(By.CSS_SELECTOR, value="input[value='radio3']")


        #Act

        radiobutton1.click()
        self.assertEqual(self.driver.find_element(By.CSS_SELECTOR, value="input:checked").get_attribute("value"),
                         "radio1")

        radiobutton2.click()
        self.assertEqual(self.driver.find_element(By.CSS_SELECTOR, value="input:checked").get_attribute("value"),
                         "radio2")

        radiobutton3.click()
        self.assertEqual(self.driver.find_element(By.CSS_SELECTOR, value="input:checked").get_attribute("value"),
                         "radio3")



        #Assert

        #erfolgsmeldung =self.driver.find_element(By.CSS_SELECTOR, value = "#droppable > p").text
        #self.assertTrue("blue-logo" in erfolgsmeldung)

    if __name__=='__main__':
        unittest.main()
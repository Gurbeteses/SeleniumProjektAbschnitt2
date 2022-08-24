import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class TestElementeCheckBoxSeleniumKursFireFox(unittest.TestCase):

    def setUp(self):
        print("Initialisiere WebDriver für den Test")
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://seleniumkurs.codingsolo.de")

    def tearDown(self):
        print("Nach dem Test. Ich räume auf")
        self.driver.close()

    def test_radio_button(self):
        print("Starte test_check_box")


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

        checkBox1 = self.driver.find_element(By.ID, value="checkBoxOption1")
        checkBox2 = self.driver.find_element(By.ID, value="checkBoxOption2")
        checkBox3 = self.driver.find_element(By.ID, value="checkBoxOption3")



        #Act

        checkBox1.click()
        checkBox1.click()
        checkBox2.click()
        checkBox3.click()

        #Assert

        self.assertEqual(checkBox1.is_selected(),False)
        self.assertEqual(checkBox2.is_selected(),True)
        self.assertEqual(checkBox3.is_selected(),True)

    if __name__=='__main__':
        unittest.main()
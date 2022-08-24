import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class TestElementeIFrameSeleniumKursFireFox(unittest.TestCase):

    def setUp(self):
        print("Initialisiere WebDriver für den Test")
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://seleniumkurs.codingsolo.de")

    def tearDown(self):
        print("Nach dem Test. Ich räume auf")
        self.driver.close()

    def test_iFrame(self):
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

        linkSeleniumApp = self.driver.find_element(By.LINK_TEXT, value="IFrame Beispiel")
        linkSeleniumApp.click()

        self.driver.switch_to.frame(self.driver.find_element(By.ID, value="iframe"))

        #Starte Radio Button

        inputName = self.driver.find_element(By.ID, value="name")
        buttonalert = self.driver.find_element(By.ID, value="alertbtn")

        #Act

        inputName.send_keys("Dieter")
        buttonalert.click()

        #Assert

        self.assertTrue('42' in self.driver.switch_to.alert.text)
        #self.driver.switch_to.alert.accept()


    if __name__=='__main__':
        unittest.main()
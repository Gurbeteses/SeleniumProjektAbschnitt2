import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time


class TestLoginSeleniumKursFireFox(unittest.TestCase):

    def setUp(self):
        print("Initialisiere WebDriver für den Test")
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://seleniumkurs.codingsolo.de")

    def tearDown(self):
        print("Nach dem Test. Ich räume auf")
        time.sleep(5)
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

        linkSeleniumApp = self.driver.find_element(By.LINK_TEXT, value="Drag and Drop Beispiel")
        linkSeleniumApp.click()

        #Starte Drag and Drop

        draglogo1 = self.driver.find_element(By.ID, value ="white-logo")
        draglogo2 = self.driver.find_element(By.ID, value = "red-logo")
        draglogo3 = self.driver.find_element(By.ID, value ="green-logo")
        draglogo4 = self.driver.find_element(By.ID, value ="blue-logo")

        dropbox = self.driver.find_element(By.ID, value ="droppable")

        action = ActionChains(self.driver)


        #Act

        action.drag_and_drop(draglogo1, dropbox).perform()
        action.drag_and_drop(draglogo2, dropbox).perform()

        action.drag_and_drop_by_offset(draglogo3, 250, 25 ).perform()

        action.click_and_hold(draglogo4).perform()
        action.move_to_element(dropbox).perform()
        action.release(draglogo4).perform()

        #action.click_and_hold(draglogo4).move_to_element(dropbox).release(draglogo4).perform()

        #Assert

        erfolgsmeldung =self.driver.find_element(By.CSS_SELECTOR, value = "#droppable > p").text
        self.assertTrue("blue-logo" in erfolgsmeldung)

    if __name__=='__main__':
        unittest.main()
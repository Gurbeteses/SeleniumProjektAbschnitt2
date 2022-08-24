import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

from tests.pages.seleniumkurs_login_page import SeleniumKursLoginPage


class TestLoginSeleniumKursFireFox(unittest.TestCase):

    def setUp(self):
        print("Initialisiere WebDriver für den Test")
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.google.de")
        self.driver.get("https://www.Hiq.de")
        self.driver.forward()
        self.driver.back()


    def tearDown(self):ö
        print("Nach dem Test. Ich räume auf")
        #self.driver.close()

    def test_login(self):
        print("Starte test_login")
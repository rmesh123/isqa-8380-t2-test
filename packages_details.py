import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from datetime import date, timedelta
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class packages_details(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_aafr(self):

        user = "team2"
        pwd = "cloud123"
        homepage = "http://vahini.pythonanywhere.com/"

        driver = self.driver
        driver.maximize_window()
        driver.get("http://vahini.pythonanywhere.com/accounts/login/")
        elem = driver.find_element(By.NAME, "username")
        elem.send_keys(user)
        elem = driver.find_element(By.NAME, "password")
        elem.send_keys(pwd)
        elem = driver.find_element(By.XPATH,"/html/body/div/form/div[1]/div/input")
        elem.click()
        time.sleep(2)
        elem = driver.find_element(By.XPATH,"/html/body/div/form/div[2]/div/input")
        elem.click()
        time.sleep(2)
        elem = driver.find_element(By.XPATH,"/html/body/div/form/input[2]")
        elem.click()
        time.sleep(2)
        elem = driver.find_element(By.XPATH, "/html/body/div/table[2]/tbody/tr[1]/td[1]/a")
        elem.click()
        time.sleep(3)



    @classmethod
    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
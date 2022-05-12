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
        user = "instructor"
        pwd = "gounomavs1a"
        homepage = "https://isqa-8380-t2.herokuapp.com/"

        driver = self.driver
        driver.maximize_window()
        driver.get("https://isqa-8380-t2.herokuapp.com/accounts/login/")
        elem = driver.find_element(By.NAME, "username")
        elem.send_keys(user)
        elem = driver.find_element(By.NAME, "password")
        elem.send_keys(pwd)
        elem = driver.find_element(By.XPATH,"/html/body/div/form/div[1]/div/input")
        elem.click()
        time.sleep(1)
        elem = driver.find_element(By.XPATH,"/html/body/div/form/div[2]/div/input")
        elem.click()
        time.sleep(1)
        elem = driver.find_element(By.XPATH,"/html/body/div/form/input[2]")
        elem.click()
        time.sleep(1)
        elem = driver.find_element(By.XPATH, "/html/body/div/table[2]/tbody/tr[1]/td[1]/a")
        elem.click()
        time.sleep(1)
        elem = driver.find_element(By.XPATH, "/html/body/div[2]/a")
        elem.click()
        time.sleep(1)
        elem = driver.find_element(By.XPATH, "/html/body/div/div/div[1]/table/tbody/tr/th[3]/a")
        elem.click()
        time.sleep(1)
        elem = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/form/div[2]/div[1]/input")
        elem.send_keys("111122223333344444")
        time.sleep(1)
        elem = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/form/div[2]/div[2]/input")
        elem.send_keys("07/22/2025")
        time.sleep(1)
        elem = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/form/div[2]/div[3]/input")
        elem.send_keys("10672 lafayette plz")
        time.sleep(1)
        elem = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/form/div[2]/div[4]/input")
        elem.send_keys("Omaha")
        time.sleep(1)
        elem = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/form/div[2]/div[5]/input")
        elem.send_keys("NE")
        time.sleep(1)
        elem = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/form/div[2]/div[6]/input")
        elem.send_keys("68005")
        time.sleep(1)
        # elem = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/form/input")
        # elem.click()
        # time.sleep(1)

    @classmethod
    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()




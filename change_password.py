import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class change_password(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_aafr(self):

        user = "rdanuwar6"
        pwd = "cloud12345"
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
        time.sleep(2)
        elem = driver.find_element(By.XPATH,"/html/body/div/form/div[2]/div/input")
        elem.click()
        time.sleep(2)
        elem = driver.find_element(By.XPATH,"/html/body/div/form/input[2]")
        elem.click()
        time.sleep(2)
        elem = driver.find_element(By.XPATH, "/html/body/nav/div/ul/li[1]/a")
        elem.click()
        time.sleep(2)
        elem = driver.find_element(By.XPATH, "/html/body/form/div[1]/div/input")
        elem.send_keys("cloud12345")
        time.sleep(3)
        elem = driver.find_element(By.XPATH, "/html/body/form/div[2]/div/input")
        elem.send_keys("cloud12")
        time.sleep(3)
        elem = driver.find_element(By.XPATH, "/html/body/form/div[3]/div/input")
        elem.send_keys("cloud12")
        time.sleep(3)
        elem = driver.find_element(By.XPATH, "/html/body/form/p/input")
        elem.click()
        time.sleep(2)

    @classmethod
    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

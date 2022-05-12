import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class signup(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_aafr(self):

        homepage = "https://isqa-8380-t2.herokuapp.com/"

        driver = self.driver
        driver.maximize_window()
        driver.get("https://isqa-8380-t2.herokuapp.com/")
        elem = driver.find_element(By.XPATH, "/html/body/nav/div/ul/li[1]/a")
        elem.click()
        time.sleep(3)
        elem = driver.find_element(By.XPATH, "/html/body/div/form/p[1]/input")
        elem.send_keys("rdanuwar6")
        time.sleep(3)
        elem = driver.find_element(By.XPATH, "/html/body/div/form/p[2]/input")
        elem.send_keys("cloud12345")
        time.sleep(3)
        elem = driver.find_element(By.XPATH, "/html/body/div/form/p[4]/input")
        elem.send_keys("cloud12345")
        time.sleep(3)
        elem = driver.find_element(By.XPATH, "/html/body/div/form/button")
        elem.click()
        time.sleep(4)







    @classmethod
    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()



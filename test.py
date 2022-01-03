from enum import Flag
from typing import List
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class MyTest(unittest.TestCase):
    url = "http://localhost:3000"

    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=s)

    # Test if list of cars is shown on /
    def test_getAllCars(self):
        driver = self.driver
        driver.get(self.url)

        try:
            listElement = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'list')]"))
            )
            assert True
        except:
            assert False, "List of cars couldn't be loaded within 10 seconds."
    
    # Test if list of cars is shown after country selection on /brandsbycountry
    def test_getBrandsByCountry(self):
        driver = self.driver
        driver.get(self.url+"/brandsbycountry")

        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//select//option/following-sibling::option"))
            )
            driver.find_element_by_xpath("//select//option[2]").click()
            try:
                listElement = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'list')]"))
                )
                assert True
            except:
                assert False, "List of cars couldn't be loaded within 10 seconds."
        except:
            assert False, "Select list of countries couldn't be loaded within 10 seconds or was empty."

    # Test if list of cars is shown after year selection on /modelsbyyear
    def test_getModelsByYear(self):
        driver = self.driver
        driver.get(self.url+"/modelsbyyear")

        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//select//option/following-sibling::option"))
            )
            driver.find_element_by_xpath("//select//option[2]").click()
            try:
                listElement = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'list')]"))
                )
                assert True
            except:
                assert False, "List of cars couldn't be loaded within 10 seconds."
        except:
            assert False, "Select list of years couldn't be loaded within 10 seconds or was empty."
    
    # Test if list of cars is shown after type selection on /modelsbytype
    def test_getModelsByType(self):
        driver = self.driver
        driver.get(self.url+"/modelsbytype")

        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//select//option/following-sibling::option"))
            )
            driver.find_element_by_xpath("//select//option[2]").click()
            try:
                listElement = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'list')]"))
                )
                assert True
            except:
                assert False, "List of cars couldn't be loaded within 10 seconds."
        except:
            assert False, "Select list of types couldn't be loaded within 10 seconds or was empty."

    # Test create brand
    def test_createBrand(self):
        driver = self.driver
        driver.get(self.url)

        inputCreateName = driver.find_element_by_xpath("//div[contains(@class, 'wrapper-create-form')]//input[@id='name']")
        inputCreateCountry = driver.find_element_by_xpath("//div[contains(@class, 'wrapper-create-form')]//input[@id='country']")
        inputCreateFoundingYear = driver.find_element_by_xpath("//div[contains(@class, 'wrapper-create-form')]//input[@id='foundingYear']")

        inputCreateName.clear()
        inputCreateName.send_keys("Brand created by Selenium")
        inputCreateCountry.clear()
        inputCreateCountry.send_keys("Greece")
        inputCreateFoundingYear.clear()
        inputCreateFoundingYear.send_keys("2005")

        driver.find_element_by_xpath("//div[contains(@class, 'wrapper-create-form')]//input[@type='submit']").click()

        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'Toastify')]//div[text()='Brand created']"))
            )
            assert True
        except:
            assert False, "Creating took too long or resulted in an error."

    # Test update brand
    def test_updateBrand(self):
        driver = self.driver
        driver.get(self.url)

        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'car')]//button[contains(@title, 'Edit')]"))
            )
            
            driver.find_element_by_xpath("(//div[contains(@class, 'car')]//button[contains(@title, 'Edit')])[1]").click()

            inputUpdateName = driver.find_element_by_xpath("//div[contains(@class, 'wrapper-update-form')]//input[@id='name']")
            inputUpdateCountry = driver.find_element_by_xpath("//div[contains(@class, 'wrapper-update-form')]//input[@id='country']")
            inputUpdateFoundingYear = driver.find_element_by_xpath("//div[contains(@class, 'wrapper-update-form')]//input[@id='foundingYear']")

            inputUpdateName.clear()
            inputUpdateName.send_keys("Brand updated by Selenium")
            inputUpdateCountry.clear()
            inputUpdateCountry.send_keys("Portugal")
            inputUpdateFoundingYear.clear()
            inputUpdateFoundingYear.send_keys("1968")

            driver.find_element_by_xpath("//div[contains(@class, 'wrapper-update-form')]//input[@type='submit']").click()

            try:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'Toastify')]//div[text()='Brand updated']"))
                )
                assert True
            except:
                assert False, "Updating took too long or resulted in an error."
        except:
            assert False, "No edit button found or loading took too long."

    # Todo: add delete model test as soon as brand-service back working
    def test_deleteModel(self):
        driver = self.driver
        driver.get(self.url)

        try:
            listElement = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'car')]//div[contains(@class, 'model')]//button[contains(@title, 'Delete')]"))
            )
            driver.find_element_by_xpath("(//div[contains(@class, 'car')]//div[contains(@class, 'model')]//button[contains(@title, 'Delete')])[1]").click()
            try:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'Toastify')]//div[text()='Model deleted']"))
                )
                assert True
            except:
                assert False, "Deleting took too long or resulted in an error."
        except:
            assert False, "No delete button found or loading took too long."

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
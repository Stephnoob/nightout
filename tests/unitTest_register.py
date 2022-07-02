# Unit test to see if Create Event page displays properly
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import warnings


class ll_ATS(unittest.TestCase):
    # set up the test class - assign the driver to Chrome - if using a different
    # browser, change the browser name below
    def setUp(self):
        self.driver = webdriver.Chrome()
        warnings.simplefilter('ignore', ResourceWarning)  # ignore resource warning if occurs

    # Test if Create event is displayed when clicked in the Navigation bar
    def test_ll(self):

        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000")
        time.sleep(3)  # pause to allow screen to load

        # Here we will find the element for the Register Page
        elem = driver.find_element(By.XPATH, '//*[@id="navbarCollapse"]/ul/li[5]/a').click()
        time.sleep(3)  # pause to allow screen to change

        # Data to be filled in
        Name = "Andrew Matthiessen"
        Email = "andrewjmatt@yahoo.com"
        Password = "NightOut123"

        # Here we will fill out all the data for registering
        elem = driver.find_element(By.XPATH, '//*[@id="id_username"]')
        elem.send_keys(Name)
        time.sleep(1)
        elem = driver.find_element(By.XPATH, '//*[@id="id_email"]')
        elem.send_keys(Email)
        time.sleep(1)
        elem = driver.find_element(By.XPATH, '//*[@id="id_password1"]')
        elem.send_keys(Password)
        time.sleep(1)
        elem = driver.find_element(By.XPATH, '//*[@id="id_password2"]')
        elem.send_keys(Password)
        time.sleep(1)

        elem = driver.find_element(By.XPATH, '//*[@id="card"]/div/form/input[6]').click()
        time.sleep(3)  # pause to allow screen to change
        # Here we verify if the event is good


        try:
            # verify Summary button exists on new screen after clicking "Customers" button
            elem = driver.find_element(By.XPATH,
                                       '//*[@id="card"]/div/h2')
            print("Test passed - Registration worked")
            assert True

        except NoSuchElementException:
            self.fail("Registration didnt work - test failed")


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()

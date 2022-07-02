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
        user = "amatthiessen"  # must be a valid username for the application
        pwd = "harambe321"  # must be the password for a valid user

        # Here is the navigation to the page
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000")
        time.sleep(3)  # pause to allow screen to load

        # find the username and password input boxes on the screen by ID
        # send the username and password to each box
        # send the Return (Enter) key to the system
        # go to the main application page
        elem = driver.find_element(By.XPATH, '//*[@id="card"]/div/form/input[2]')
        elem.send_keys(user)
        elem = driver.find_element(By.XPATH, '//*[@id="card"]/div/form/input[3]')
        elem.send_keys(pwd)
        time.sleep(3)
        elem.send_keys(Keys.RETURN)
        time.sleep(3)
        driver.get("http://127.0.0.1:8000")
        time.sleep(3)

        # Next we are going to navigate to the Create Event Page
        elem = driver.find_element(By.XPATH, '//*[@id="navbarCollapse"]/ul/li[2]/a').click()
        time.sleep(3)  # pause to allow screen to change
        try:
            # verify Summary button exists on new screen after clicking "Customers" button
            elem = driver.find_element(By.XPATH,
                                       '/html/body/main/div/div/h3')
            print("Test passed - Create Event displayed")
            assert True

        except NoSuchElementException:
            self.fail("Create Event does not appear when Create Event Tab is clicked - test failed")


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()

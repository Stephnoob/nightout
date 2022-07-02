# Selenium test script
# test script to verify a valid user is logged in successfully
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

import warnings


class ll_ATS(unittest.TestCase):
    # set up the test class - assign the driver to Chrome - if using a different
    # browser, change the browser name below
    def setUp(self):
        self.driver = webdriver.Chrome()
        warnings.simplefilter('ignore', ResourceWarning)  # ignore resource warning if occurs

    # If login is successful, 'Logout' will be displayed as the text in the Navbar
    def test_ll(self):
        user = "amatthiessen"  # must be a valid username for the application
        pwd = "harambe321"  # must be the password for a valid user
        members = "test1@gmail.com"
        name = "Karaoke Night"
        Location1 = "Midtown"
        Location2 = "Downtown"
        Location3 = "Mall"
        Time1 = "7/1/2022"
        Time2 = "7/2/2022"
        Time3 = "7/3/2022"
        endtime = "7/4/2022"

        # open the browser and go to the admin page
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/")


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

        # Now we are going to fill out event details
        select = Select(driver.find_element(By.ID, "id_creator"))
        select.select_by_index(12)
        time.sleep(1)
        elem = driver.find_element(By.ID, "id_member")
        elem.send_keys(members)
        time.sleep(1)
        elem = driver.find_element(By.ID, "id_event_name")
        elem.send_keys(name)
        time.sleep(1)
        elem = driver.find_element(By.ID, "id_location1")
        elem.send_keys(Location1)
        time.sleep(1)
        elem = driver.find_element(By.ID, "id_location2")
        elem.send_keys(Location2)
        time.sleep(1)
        elem = driver.find_element(By.ID, "id_location3")
        elem.send_keys(Location3)
        time.sleep(1)
        elem = driver.find_element(By.ID, "id_time1")
        elem.clear()
        elem.send_keys(Time1)
        time.sleep(1)
        elem = driver.find_element(By.ID, "id_time2")
        elem.clear()
        elem.send_keys(Time2)
        time.sleep(1)
        elem = driver.find_element(By.ID, "id_time3")
        elem.clear()
        elem.send_keys(Time3)
        time.sleep(3)
        elem = driver.find_element(By.ID, "id_end_time")
        elem.clear()
        elem.send_keys(endtime)
        time.sleep(3)

        elem = driver.find_element(By.XPATH, '/html/body/main/div/div/form/button').click()
        time.sleep(3)

        # Here we verfiy if the event is good
        try:
            # verify Summary button exists on new screen after clicking "Customers" button
            elem = driver.find_element(By.XPATH,
                                       '/html/body/main/div[2]/h1')
            print("Test passed - Create Event worked")
            assert True

        except NoSuchElementException:
            self.fail("Create Event didnt work - test failed")



def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()

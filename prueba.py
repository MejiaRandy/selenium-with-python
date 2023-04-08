import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Import of Exceptions in case of need for handling.
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import WebDriverException

from PIL import Image

class myTests():
    usernameInput = None
    passwordInput = None

    def __init__(self, username, password):
        # Driver initiliaze to open browser (Chrome).
        self.driver = webdriver.Chrome()

        # instance attributes
        self.username = username
        self.password = password

    # Goes to the URL provided.
    def logInTest(self):
        self.driver.get("https://www.saucedemo.com/")

        # Looks for elements (username, password) on website form.
        self.usernameInput = self.driver.find_element(By.ID, "user-name")
        self.usernameInput.send_keys("standard_user")

        self.passwordInput = self.driver.find_element(By.ID, "password")
        self.passwordInput.send_keys("secret_sauce")

        if self.username == "standard_user1" and self.password == "secret_sauce":
            # changes URL after logIn button is clicked
            loginButton = self.driver.find_element(By.ID, "login-button").click()
            self.driver.get("https://www.saucedemo.com/inventory.html")
            self.driver.save_screenshot('images/tests/logIn/logSucessful.png')
            self.driver.quit()

        else:
            print("Username or Password doesn't match!, try again.")
            self.driver.save_screenshot('images/tests/logIn/logFail.png')
            self.driver.quit()

try:
    testOne = myTests("standard_user", "secret_sauce")
    testOne.logInTest()
except Exception as e:
    print(e)    
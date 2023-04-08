import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Import of Exceptions in case of need for handling.
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import WebDriverException

class myTests():
    def __init__(self):
        # Driver initiliaze to open browser (Chrome).
        self.driver = webdriver.Chrome()

    # Goes to the URL provided.
    def logInTest(self):
        self.driver.get("https://www.saucedemo.com/")

        # Correct username and password values to log in.
        username = "standard_user"
        password = "secret_sauce"

        # Looks for elements (username, password) on website form.
        usernameInput = self.driver.find_element(By.ID, "user-name").send_keys("standard_user")

        passwordInput = self.driver.find_element(By.ID, "password").send_keys("secret_sauce")

        if username == "standard_user" and password == "secret_sauce":
            # changes URL after logIn button is clicked and prints a screenshot of success!
            loginButton = self.driver.find_element(By.ID, "login-button").click()
            self.driver.get("https://www.saucedemo.com/inventory.html")
            self.driver.save_screenshot('images/tests/logIn/logSucessful.png')
        else:
            # If fails then prints a screenshot of fail.
            print("Username or Password doesn't match!, try again.")
            self.driver.save_screenshot('images/tests/logIn/logFail.png')
            self.driver.quit()
    
    def addToCartTest(self):
        addBackpackToCart = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        addShirtToCart = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.save_screenshot('images/tests/itemCart/addToCart/addToCartSuccess.png')

    def goToCheckOut(self):
        # Clicks the Cart Icon to go to Details.
        openCart = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        self.driver.get("https://www.saucedemo.com/cart.html")

        # Gets to checkout 
        clickCheckOutButton = self.driver.find_element(By.ID, "checkout").click()
        self.driver.get("https://www.saucedemo.com/checkout-step-one.html")

        self.driver.save_screenshot('images/tests/checkout/goToCheckOut/goToCheckOutSuccess.png')

    def completeCheckOut(self):
        first_name = self.driver.find_element(By.ID, "first-name").send_keys("Randy")

        last_name = self.driver.find_element(By.ID, "last-name").send_keys("Mejia")

        postal_code = self.driver.find_element(By.ID, "postal-code").send_keys("10101")

        self.driver.save_screenshot('images/tests/checkout/completeCheckOut/completeCheckOutSuccess.png')

        continue_button = self.driver.find_element(By.ID, "continue").click()
        self.driver.get("https://www.saucedemo.com/checkout-step-two.html")

        finish_button = self.driver.find_element(By.ID, "finish").click()
        self.driver.get("https://www.saucedemo.com/checkout-complete.html")
        self.driver.save_screenshot('images/tests/checkout/completeCheckOut/finishCheckOutSuccess.png')
        self.driver.quit()
try:
    Tests = myTests()
    Tests.logInTest()
    Tests.addToCartTest()
    Tests.goToCheckOut()
    Tests.completeCheckOut()

except Exception as e:
    print(e)  
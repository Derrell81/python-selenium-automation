from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.target.com/')

# Locate Signin
driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']").click()

# Click Signin
driver.find_element(By.XPATH, "//li[@id='listaccountNav-signIn']").click()
sleep(4)
# Verification of 'Sign into your Target Account' text
actual_text = driver.find_element(By.XPATH, "//h1[contains(@class, 'styles__AuthHeading')]").text
assert actual_text == 'Sign into your Target account'

# Verify Sign In Button
driver.find_element(By.XPATH, "//button[@type='submit']")


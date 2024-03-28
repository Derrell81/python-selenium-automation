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
driver.get('https://www.amazon.com/')

# Click Sign In Option
driver.find_element(By.XPATH, "//a[@data-nav-role='signin']").click()

#Amazon Logo
driver.find_element(By.XPATH, "//i[@aria-label='Amazon']")

#Email field
driver.find_element(By.XPATH, "//input[@name='email']")

#Continue Button
driver.find_element(By.XPATH, "//input[@aria-labelledby='continue-announce']")

# Conditions of use link
driver.find_element(By.XPATH, "//*[text()='Conditions of Use']")
sleep(3)
# Privacy Notice link
driver.find_element(By.XPATH, "//*[text()='Privacy Notice']")
sleep(3)
# Need help link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")
sleep(3)
# Forgot your password link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']").click()
driver.find_element(By.XPATH, "//a[@id='auth-fpp-link-bottom']")
sleep(3)
# Other issues with Sign-In link
driver.find_element(By.XPATH, "//a[@id='ap-other-signin-issues-link']")
sleep(3)
# Create your Amazon account button
driver.find_element(By.XPATH, "//a[@id='createAccountSubmit']")












sleep(6)
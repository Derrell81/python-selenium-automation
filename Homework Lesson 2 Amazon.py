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

# Amazon Logo
driver.find_element(By.XPATH, "//i[@aria-label='Amazon']")

# Email field
driver.find_element(By.XPATH, "//input[@name='email']")

# Continue Button
driver.find_element(By.XPATH, "//input[@aria-labelledby='continue-announce']")

# Conditions of use link
driver.find_element(By.XPATH, "//*[text()='Conditions of Use']")

# Privacy Notice link
driver.find_element(By.XPATH, "//*[text()='Privacy Notice']")

# Need help link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")

# Forgot your password link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']").click()
driver.find_element(By.XPATH, "//a[@id='auth-fpp-link-bottom']")

# Other issues with Sign-In link
driver.find_element(By.XPATH, "//a[@id='ap-other-signin-issues-link']")

# Create your Amazon account button
driver.find_element(By.XPATH, "//a[@id='createAccountSubmit']")




#Find the most optimal locators for Create Account on amazon.com (Registration) page elements:
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

# Amazon Logo
driver.find_element(By.CSS_SELECTOR, ".a-icon.a-icon-logo")

# Create Account Header
driver.find_element(By.CSS_SELECTOR, ".a-spacing-small")

# Name Field
driver.find_element(By.CSS_SELECTOR, "#ap_customer_name")

# Email Field
driver.find_element(By.CSS_SELECTOR, "#ap_email")

# Password Field
driver.find_element(By.CSS_SELECTOR, "#ap_password")

# Password Re-Enter Field
driver.find_element(By.CSS_SELECTOR, "#ap_password_check")

# Continue Button
driver.find_element(By.CSS_SELECTOR, "#continue.a-button-input")

# Conditions of Use Policy
driver.find_element(By.CSS_SELECTOR, "a[href*='ap_register_notification_condition_of_use']")

# Privacy Notice
driver.find_element(By.CSS_SELECTOR, "a[href*='register_notification_privacy_notice']")

# Sign In Link
driver.find_element(By.CSS_SELECTOR, ".a-link-emphasis")
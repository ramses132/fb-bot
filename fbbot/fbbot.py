import time
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select, WebDriverWait

driver = webdriver.Firefox()
driver.get('https://www.facebook.com/login.php?login_attempt=1&lwv=110')
print("opened facebook...")
email = driver.find_element_by_xpath("//input[@id='email' or  @name='email']")
email.send_keys('email')
print("email entered...")
password = driver.find_element_by_xpath("//input[@id='pass']")
password.send_keys('password')
print("Password entered...")
button = driver.find_element_by_xpath("//button[@id='loginbutton']")
button.click()
print("facebook opened")
status = driver.find_element_by_xpath("//textarea[@name='xhpc_message']")
status.send_keys("Bot is typing here");
print ("Status trying")
postbutton = driver.find_element_by_xpath("//button[@type='submit' and contains(.,'Publicar')]")
driver.execute_script("arguments[0].click();", postbutton)
print("post done")

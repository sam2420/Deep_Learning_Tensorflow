import sys

from selenium import webdriver


driver = webdriver.Firefox()

try:
    driver.get("http://192.168.254.1:8090/httpclient.html")
except:
    sys.exit(0)

# object has no attribute 'find_element_by_name'
# username = driver.find_element_by_name("username")
# differnt functin for the same above line is
username = driver.find_element_by_xpath("//input[@name='username']")
username.clear()

password = driver.find_element_by_name("password")
password.clear()

username.send_keys("PES2UG21CS299")
password.send_keys("PES2UG21CS299")

driver.find_element_by_id("loginbutton").click()

print("Logged in successfully")

driver.close()

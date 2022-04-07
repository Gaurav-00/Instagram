import time

from selenium import webdriver
from webdriver_manager.chrome import  ChromeDriverManager

username=input("Enter user name-:")
password=input("Enetr password-:")
driver = webdriver.Chrome(ChromeDriverManager().install())
print("Test case started")
driver.maximize_window()
driver.get("https://www.https://www.instagram.com/accounts/login")
#driver.find_element_by_name("login").send_keys("login") #to searh a  word in google
driver.find_element_by_name("username").send_keys(username) #to searh a  word in google
time.sleep(3)
driver.find_element_by_name("password").send_keys(password)
time.sleep(3)
#driver.find_element_by_class_name("qF0y9").click()
driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(5)   #time is given to hold for 5 sec

driver.close()
print("testcase successfully completed")




from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="A:\Automation\Selenium_using_python\chromedriver.exe")
driver.get("http://demo.guru99.com/test/upload/")
#driver.switch_to.frame()
driver.find_element_by_xpath("//input[@id='uploadfile_0']").send_keys("A://Automation/Selenium_using_python/Selenium_Projects/butterfly.jpg")
time.sleep(10)
driver.find_element_by_id("submitbutton").click()
time.sleep(5)
driver.close()
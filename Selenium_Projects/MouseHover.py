from selenium import webdriver
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="A:\Automation\Selenium_using_python\chromedriver.exe")
driver.get("https://www.orangehrm.com/")

res = driver.find_element_by_xpath("//a[@class='link'][normalize-space()='Resources']")
blog = driver.find_element_by_xpath("//p[@class='menu-list-name']//a[normalize-space()='The OrangeHRM Corporate Directory']")

actions = ActionChains(driver)
time.sleep(5)
actions.move_to_element(res).move_to_element(blog).click().perform()

time.sleep(5)
driver.close()
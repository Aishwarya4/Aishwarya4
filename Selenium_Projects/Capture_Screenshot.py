from selenium import webdriver

driver = webdriver.Chrome(executable_path="A:\Automation\Selenium_using_python\chromedriver.exe")
driver.get("https://alison.com/")

# driver.save_screenshot("A:\\Automation\\Selenium_using_python\\Selenium_Projects\\screenshots\\testss.png")
driver.get_screenshot_as_file("A:\\Automation\\Selenium_using_python\\Selenium_Projects\\screenshots\\testss2.png")
driver.close()
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time

# driver = webdriver.Chrome(executable_path="A:\Automation\Selenium_using_python\chromedriver.exe")
# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

driver.implicitly_wait(5)
driver.get("https://www.abhibus.com/")

driver.find_element(By.XPATH, "//*[@id='source']").send_keys("ben")
listElements = driver.find_elements(By.XPATH, "//ul[@id='ui-id-1']/li")

print("Total no of suggestions:", len(listElements))

for ele in listElements:
    print("Suggestion is:", ele.text)
    if ele.text == "Benipatti":
        print("Record Found", ele.text)
        ele.click()
        break

time.sleep(5)
driver.close()

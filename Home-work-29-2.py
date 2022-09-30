from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

options = Options()
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(service=Service('/Users/yulia/Desktop/Hillel/Selenium_WebDriver/chromedriver'), options=options)

user = "guest"
password = "welcome2qauto"
driver.get("https://" + user + ":" + password + "@" + "qauto2.forstudy.space/")
# driver.get("https://qauto2.forstudy.space/")

# time.sleep(3)  # sleep for 3 sec

# WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Sign In')]"))).click()

# def is_element_present(self, how, what):
#    try:
#       self.driver.find_element(by=how, value=what)
#    except NoSuchElementException as e:
#        return False
#    return True


try:
    element = driver.find_element(By.XPATH, "//html/body/app-root/app-global-layout")
except NoSuchElementException:
    print("No element found")

element = driver.find_element(By.XPATH, '//html/body/app-root/app-global-layout')  # this element is visible
if element.is_displayed():
    print("Element found")
    not_found = True
else:
    print("Element not found")
    not_found = False

assert "Do more!" not in driver.current_window_handle
assert not_found

driver.close()

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

base_url = "https://facebook.com"
chrome_driver_path = r"C:\Users\nthallap\Downloads\drivers\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.implicitly_wait(20)
driver.set_page_load_timeout(50)
driver.get(base_url)

window_height = driver.execute_script("return window.innerHeight;")
window_width = driver.execute_script("return window.innerWidth")
print(window_height, window_width)

driver.maximize_window()

window_height = driver.execute_script("return window.innerHeight;")
window_width = driver.execute_script("return window.innerWidth")
print(window_height, window_width)

email_filed = driver.find_element(By.XPATH, "//input[@id='email']")
password_field = driver.find_element(By.CSS_SELECTOR, "#pass")
submit_field = driver.find_element(By.XPATH,"//button[contains(text(), 'Log In')]")

email_filed.send_keys("TEST@outlook.com")
password_field.send_keys("test123")
submit_field.click()

time.sleep(5)
# alert = driver.switch_to.
# alert.dismiss()

for i in range(0, 10000,20):
    driver.execute_script("window.scrollBy(0, {});".format(i))
    time.sleep(1)


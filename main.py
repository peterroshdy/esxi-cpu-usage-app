from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

## Ignore certs and run in background
options = webdriver.ChromeOptions()
options.add_argument('ignore-certificate-errors')
options.add_argument("headless")

## Load driver from the path, Chrome Driver 90
driver = webdriver.Chrome(executable_path='./chromedriver.exe', chrome_options=options)

url = 'URL_TO_THE_VM_ON_ESXI'
driver.get(url)

wait = WebDriverWait(driver,10)

## Fill username
driver.execute_script('arguments[0].click();',wait.until(EC.element_to_be_clickable((By.ID, 'username'))))
wait.until(EC.element_to_be_clickable((By.ID, 'username'))).send_keys("ENTER_USERNAME")

## Fill password
driver.execute_script('arguments[0].click();',wait.until(EC.element_to_be_clickable((By.ID, 'password'))))
wait.until(EC.element_to_be_clickable((By.ID, 'password'))).send_keys("ENTER_PASSWORD")

## Click login
driver.execute_script('arguments[0].click();',wait.until(EC.element_to_be_clickable((By.ID, 'submit'))))

## Wait 10 seconds to login successfully
sleep(10)

## Hit ESC key to remove any pop-ups
webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

## Hit the Refresh button to get latest reading
driver.execute_script('arguments[0].click();',wait.until(EC.element_to_be_clickable((By.ID, '1'))))
sleep(10)

## Take a screenshot
driver.get_screenshot_as_file("screenshot.png")
driver.quit()
print("Success...")
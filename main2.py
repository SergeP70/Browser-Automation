import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# Define driver, options and service
chrome_options = Options()
chrome_options.add_argument('--disable-search-engine-choice-screen')

# Select download directory
download_path = os.getcwd()
prefs = {'download.default_directory': download_path}
chrome_options.add_experimental_option('prefs', prefs)

# define driver
service = Service('chromedriver-mac-arm64/chromedriver')
driver = webdriver.Chrome(options=chrome_options, service=service)

# Load the webpage
driver.get('https://demoqa.com/login')

# Locate username, password and login button
username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
# login_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'login')))
# If there are dynamically adds:
login_button = driver.find_element(By.ID, 'login')

# Fill in username, password and click the button
username_field.send_keys('SergeP70')
password_field.send_keys('&^4ePvdG$bemvP')
# login_button.click()
# If there are dynamically adds:
driver.execute_script("arguments[0].click();", login_button)

# Locate the Elements dropdown and Text Box
elements = (WebDriverWait(driver, 10).
            until(EC.visibility_of_element_located((By.XPATH,'//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div'))))
elements.click()
text_box = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-0')))
text_box.click()

# Locate the Form fields
fullname_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
email_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userEmail')))
cur_address_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'currentAddress')))
perm_address_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'permanentAddress')))
submit_button = driver.find_element(By.ID, 'submit')

# Fill in the Form fields
fullname_field.send_keys('John Smith')
email_field.send_keys('john@gmail.com')
cur_address_field.send_keys('Johnstreet 100, New York, USA')
perm_address_field.send_keys('Smithstreet 200, New York, USA')
driver.execute_script("arguments[0].click();", submit_button)

# download image
download_box = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-7')))
download_box.click()
download_button = driver.find_element(By.ID, 'downloadButton')
download_button.click()

# End the program
input("Press Enter to close the browser")
driver.quit()



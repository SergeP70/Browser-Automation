import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class WebAutomation:
    def __init__(self):
        # Define driver, options and service
        chrome_options = Options()
        chrome_options.add_argument('--disable-search-engine-choice-screen')

        # Select download directory
        download_path = os.getcwd()
        prefs = {'download.default_directory': download_path}
        chrome_options.add_experimental_option('prefs', prefs)

        # define driver
        service = Service('chromedriver-mac-arm64/chromedriver')
        self.driver = webdriver.Chrome(options=chrome_options, service=service)

    def login(self, username, password):
        # Load the webpage
        self.driver.get('https://demoqa.com/login')

        # Locate username, password and login button
        username_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
        password_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
        login_button = self.driver.find_element(By.ID, 'login')

        # Fill in username, password and click the button
        username_field.send_keys(username)
        password_field.send_keys(password)
        self.driver.execute_script("arguments[0].click();", login_button)

    def fill_form(self, fullname, email, current_address, permanent_address):
        # Locate the Elements dropdown and Text Box
        elements = (WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div'))))
        elements.click()
        text_box = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-0')))
        text_box.click()

        # Locate the Form fields
        fullname_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
        email_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userEmail')))
        cur_address_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'currentAddress')))
        perm_address_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'permanentAddress')))
        submit_button = self.driver.find_element(By.ID, 'submit')

        # Fill in the Form fields
        fullname_field.send_keys(fullname)
        email_field.send_keys(email)
        cur_address_field.send_keys(current_address)
        perm_address_field.send_keys(permanent_address)
        self.driver.execute_script("arguments[0].click();", submit_button)

    def download(self):
        # download image
        download_box = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-7')))
        download_box.click()
        download_button = self.driver.find_element(By.ID, 'downloadButton')
        self.driver.execute_script("arguments[0].click();", download_button)

        # Wait for the image to download
        time.sleep(2)

    def close(self):
        self.driver.quit()



if __name__ == '__main__':
    webautomation = WebAutomation()
    webautomation.login('SergeP70', '&^4ePvdG$bemvP')
    webautomation.fill_form('John Smith', 'john@gmail.com', 'Johnstreet 100, New York, USA', 'Smithstreet 200, New York, USA')
    webautomation.download()
    webautomation.close()


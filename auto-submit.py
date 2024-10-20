import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Load the sample data from data.json file
def load_sample_data(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)
# Replace with your JSON data path
sample_data_list = load_sample_data('./data.json')

chrome_options = Options()
# Run in headless mode for background execution
# chrome_options.add_argument("--headless")

# Replace with your ChromeDriver path
service = Service(executable_path='./chromedriver')  
driver = webdriver.Chrome(service=service, options=chrome_options)

for sample_data in sample_data_list:
    driver.get("https://ck.hdm3.in/lp.php?sid=085aaaf6&txnid=uniqueid")  # Replace 'uniqueid' if dynamic

    try:
        # Wait until the name input field is present and enabled
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.NAME, "lead_data[name]"))
        )
        # Fill the name
        name_input = driver.find_element(By.NAME, "lead_data[name]")
        name_input.send_keys(sample_data['name'])
        # Wait for email input to become clickable
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.NAME, "lead_data[email]"))
        )
        # Fill the email
        email_input = driver.find_element(By.NAME, "lead_data[email]")
        email_input.send_keys(sample_data['email'])
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.NAME, "lead_data[contact_no]"))
        )
        # Fill the phone number
        phone_input = driver.find_element(By.NAME, "lead_data[contact_no]")
        phone_input.send_keys(sample_data['contact_no'])
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "btn-dark"))
        )
        submit_button = driver.find_element(By.CLASS_NAME, "btn-dark")
        submit_button.click()
        time.sleep(1)
        print(f"Form submitted successfully for {sample_data['name']}!")
    except Exception as e:
        print(f"An error occurred for {sample_data['name']}: {e}")
    finally:
        # Proceed to the next lead
        continue
driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time
import os

class Learn:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.action = ActionChains(self.driver)

    def login_webdrive(self):
        self.driver.get("https://testautomationpractice.blogspot.com/2018/09/automation-form.html")
        time.sleep(5)

        try:
            title_validation = self.driver.find_element(By.XPATH, "//h3[@class='post-title entry-title']/a").click()
            print(title_validation)
        except (NoSuchElementException, ElementClickInterceptedException):
            print("Heading element not found")

    def name_validation(self):
        if self.driver.find_element(By.ID, 'name').is_displayed():
            self.driver.find_element(By.ID, 'name').send_keys("Swetha Senthilvel")
            print("Entered the name in the input box successfully")
        else:
            print("Name input box not found")

    def email(self):
        if self.driver.find_element(By.ID, 'email').is_displayed():
            self.driver.find_element(By.ID, 'email').send_keys("swethasenthilvel@gmail.com")
            print("Entered the email in the input box successfully")
        else:
            print("Email input box not found")

    def phone(self):
        if self.driver.find_element(By.ID, 'phone').is_displayed():
            self.driver.find_element(By.ID, 'phone').send_keys("9876543210")
            print("Entered the phone number successfully")
        else:
            print("Phone input box not found")

    def gender(self):
        self.driver.find_element(By.ID, 'female').click()
        if self.driver.find_element(By.ID, 'female').is_selected():
            print("Gender selection successful")
        else:
            print("Gender selection failed")

    def drop_valid(self):
        country_dropdown = self.driver.find_element(By.ID, "country")
        selection = Select(country_dropdown)
        selection.select_by_value("canada")

    def date_pack(self):
        self.driver.find_element(By.XPATH, "//input[@id='txtDate']").click()
        time.sleep(2)
        
        month = Select(self.driver.find_element(By.XPATH, "//select[@aria-label='Select month']"))
        month.select_by_value("4")

        year = Select(self.driver.find_element(By.XPATH, "//select[@aria-label='Select year']"))
        year.select_by_value("2024")

        self.driver.find_element(By.XPATH, "//a[text()='12']").click()

    def validate_file_existence(self):
        file_path = "C:\\Users\\ramya\\Downloads\\info.txt"
        if os.path.exists(file_path):
            print("File found")
        else:
            print("File not found")

play = Learn()
play.login_webdrive()
play.name_validation()
play.email()
play.phone()
play.gender()
play.drop_valid()
play.date_pack()
play.validate_file_existence()

from datetime import datetime
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Hosttest(TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.live_server_url = 'http://127.0.0.1:8000/'

    def tearDown(self):
        self.driver.quit()
        
    def test_01_login_page(self):
        driver = self.driver
        driver.get(self.live_server_url)
        driver.maximize_window()
        time.sleep(1)
        user=driver.find_element(By.CSS_SELECTOR,"input[name='username']")
        user.send_keys("stephin")
        password=driver.find_element(By.CSS_SELECTOR,"input[name='password']")
        password.send_keys("Johnson@123")
        time.sleep(2)
        submit=driver.find_element(By.CSS_SELECTOR,"button.login-button")
        submit.click()
        time.sleep(2)
        find=driver.find_element(By.CSS_SELECTOR,"a[href='/therapists']")
        find.click()
        time.sleep(4)
        appointment=driver.find_element(By.CSS_SELECTOR,"a.book-appointment-btn[href='/book_appointment/35/']")
        appointment.click()
        time.sleep(4)
        selectdate=driver.find_element(By.CSS_SELECTOR,"input#appointment_date[type='datetime-local']")
        selectdate.click()
        time.sleep(4)



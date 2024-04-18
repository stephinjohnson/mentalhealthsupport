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
        user.send_keys("vis")
        password=driver.find_element(By.CSS_SELECTOR,"input[name='password']")
        password.send_keys("Vishnu@123")
        time.sleep(2)
        submit=driver.find_element(By.CSS_SELECTOR,"button.login-button")
        submit.click()
        # time.sleep(2)
        # add=driver.find_element(By.CSS_SELECTOR,"a.btn.btn-primary[href='/add_article/']")
        # add.click()
        # title=driver.find_element(By.CSS_SELECTOR,"input#id_title[type='text'][name='title']")
        # title.send_keys(" test product")
        # desc=driver.find_element(By.CSS_SELECTOR,"textarea#id_description[name='description']")
        # desc.send_keys("This is a test product")
        # time.sleep(2)
        # added=driver.find_element(By.CSS_SELECTOR,"button.btn.btn-primary[type='submit']")
        # added.click()
        # time.sleep(2)


        # find=driver.find_element(By.CSS_SELECTOR,"a[href='/therapists']")
        # find.click()
        # time.sleep(4)
        # appointment=driver.find_element(By.CSS_SELECTOR,"a.book-appointment-btn[href='/book_appointment/35/']")
        # appointment.click()
        # time.sleep(4)
        # selectdate=driver.find_element(By.CSS_SELECTOR,"input#appointment_date[type='datetime-local']")
        # selectdate.click()
        # time.sleep(4)
        # rev=driver.find_element(By.CSS_SELECTOR,"a[href='/write_experience']")
        
        # rev.click()
        # time.sleep(2)
        # title=driver.find_element(By.CSS_SELECTOR,"input#title")
        # title.send_keys("Sample title")
        # dis=driver.find_element(By.CSS_SELECTOR,"textarea#content")
        # dis.send_keys("Sample Review")
        # sub=driver.find_element(By.CSS_SELECTOR,"button[type='submit']")
        # sub.click()
        # time.sleep(3)
        #add time slot test
        # addtimeslot=driver.find_element(By.CSS_SELECTOR,"a.btn.btn-primary[href='/add_time_slot/']")
        # addtimeslot.click()
        # addslot=driver.find_element(By.CSS_SELECTOR,"label[for='slot1']")
        # addslot.click()
        # selectdate=driver.find_element(By.CSS_SELECTOR,"input#start_date[type='date'][name='start_date'].form-control[required]")
        # selectdate.click()
        # selectdate.send_keys('20-04-2024')
        # addbtn=driver.find_element(By.CSS_SELECTOR,"button#submit_button.btn.btn-primary[type='submit']")
        # addbtn.click()
        # time.sleep(2)
        # #View time slot test
        # viewtimeslot=driver.find_element(By.CSS_SELECTOR,"a.btn.btn-secondary[href='/new_view_time_slots/']")
        # viewtimeslot.click()


        #book appointment

        # bookAppo=driver.find_element(By.CSS_SELECTOR,"a.new-card-button[href='/view_time_slots/']")
        # bookAppo.click()
        # filter=driver.find_element(By.CSS_SELECTOR,"input#dateFilter.form-control[type='date'][placeholder='Select date...']")
        # filter.click()
        # filter.send_keys('28-03-2024')
        # aply=driver.find_element(By.CSS_SELECTOR,"button.btn.btn-outline-secondary[type='button'][onclick='applyFilters()']")
        # aply.click()
        # time.sleep(5)






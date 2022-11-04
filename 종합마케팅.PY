from ctypes import POINTER
from mimetypes import init
import pyautogui as pag
import random
import pyperclip
import selenium
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

class main:
    
    def __init__(self):
        self.admin ={
            'id':'admin',
            'pw':'lqp1o2k3!'
        }
        self.driver = webdriver.Chrome(executable_path='chromedriver')
        self.driver.implicitly_wait(time_to_wait=10)
        self.url = 'https://woopsmarketing.kr/wp-admin'
        self.urlpost = 'https://woopsmarketing.kr/wp-admin/post-new.php'
        
    def login(self):
        self.driver.get(url=self.url)
        text_id = self.driver.find_element(By.ID, 'user_login')
        text_pw = self.driver.find_element(By.ID, 'user_pass')
        btn_login = self.driver.find_element(By.ID, 'wp-submit')
        text_id.send_keys(self.admin['id'])
        text_pw.send_keys(self.admin['pw'])
        btn_login.click()
        self.driver.get(url=self.urlpost)
        time.sleep(3)
        ActionChains(self.driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    
    def firstautopost(self):
        time.sleep(2)
        change1 = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[1]/div[1]/div/div[3]/div[3]/button')
        change1.click()
        time.sleep(2)
        change2 = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div[2]/button[2]')
        change2.click()
        
        time.sleep(2)
        
        self.autopost()
    def autopost(self):
        i = 0
        # b = int(input('작성할 글의 갯수를 적어주세요 : '))
        while i < 2000 :
            #치환 멘트 변수
            with open('기호.txt',encoding='UTF8') as f:
                self.rl1 = random.choice(list(f.readlines())).splitlines()[0]
            with open('기호.txt',encoding='UTF8') as f:
                self.rl2 = random.choice(list(f.readlines())).splitlines()[0]
            with open('기호.txt',encoding='UTF8') as f:
                self.rl3 = random.choice(list(f.readlines())).splitlines()[0]
            with open('기호.txt',encoding='UTF8') as f:
                self.rl4 = random.choice(list(f.readlines())).splitlines()[0]
            with open('종합2.txt',encoding='UTF8') as f:
                self.jh1 = random.choice(list(f.readlines())).splitlines()[0]
            with open('종합마케팅.txt',encoding='UTF8') as f:
                self.jm1 = random.choice(list(f.readlines())).splitlines()[0]
            with open('종합마케팅.txt',encoding='UTF8') as f:
                self.jm2 = random.choice(list(f.readlines())).splitlines()[0]
            with open('종합마케팅.txt',encoding='UTF8') as f:
                self.jm3 = random.choice(list(f.readlines())).splitlines()[0]
            with open('종합마케팅.txt',encoding='UTF8') as f:
                self.jm4 = random.choice(list(f.readlines())).splitlines()[0]
            with open('종합마케팅.txt',encoding='UTF8') as f:
                self.jm5 = random.choice(list(f.readlines())).splitlines()[0]
            with open('종합마케팅.txt',encoding='UTF8') as f:
                self.jm6 = random.choice(list(f.readlines())).splitlines()[0]
            with open('종합마케팅.txt',encoding='UTF8') as f:
                self.jm7 = random.choice(list(f.readlines())).splitlines()[0]
            with open('종합마케팅.txt',encoding='UTF8') as f:
                self.jm8 = random.choice(list(f.readlines())).splitlines()[0]
            self.id_list = ['','']
            self.id_list = self.id_list[random.randint(0,1)]
            self.randomnumber = random.randint(0, 99999)
            self.imnum = random.randint(5,410)
            self.imnum2 = random.randint(5,410)
            self.post_title = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[1]/div/div[2]/div[2]/div[3]/div[2]/h1')
            time.sleep(1.5)
            self.post_title.send_keys('{}{} {}{}'.format(self.rl1,self.jm1,self.rl2,self.jm2))
            time.sleep(1.5)
            self.post_text = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[1]/div/div[2]/div[2]/div[3]/div[2]/textarea')
            time.sleep(1.5)
            self.post_text.send_keys('{} {}<br>{}<br>{}<br>{}<br>{}<br>{}<br><br>#{}<br>#{}<br><br>{} {}<br><br>{}<br><img src="https://woopsmarketing.kr/wp-content/uploads/2022/11/marketinggoat{}.png" alt="" class="wp-image-{}"/>'.format(self.rl4,self.jm1,self.jm2,self.jm3,self.jm4,self.jm5,self.jm6,self.jm7,self.jm8,self.jh1,self.rl3,self.randomnumber,self.imnum,self.imnum2))
            time.sleep(1.5)
            self.update1 = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[1]/div/div[1]/div/div[3]/button[2]')
            time.sleep(1.5)
            self.update1.click()
            time.sleep(1.5)
            self.update2 = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[1]/div/div[2]/div[4]/div[2]/div/div/div[1]/div[1]/button')
            time.sleep(1.5)
            self.update2.click()
            time.sleep(1.5)
            self.new_post = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[1]/div/div[2]/div[4]/div[2]/div/div/div[2]/div/div[2]/div[2]/a[2]')
            time.sleep(1.5)
            self.new_post.click()
            time.sleep(1.5)
            i += 1
        
        
j = main()
j.login()
j.firstautopost()
        
from django.test import LiveServerTestCase
from django.urls import reverse_lazy
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestLogin(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Chrome()
    
    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login(self):
        # ログインページを開く
        self.selenium.get('http://localhost:8000/' + str(reverse_lazy('account_login')))

        # メールアドレス欄の入力
        username_input = self.selenium.find_element(By.NAME, "login")
        username_input.send_keys('hitsuzi@icloud.com')

        # パスワード欄の入力
        password_input = self.selenium.find_element(By.NAME, "password")
        password_input.send_keys('1234pass')

        # ログインボタンのクリック
        button = self.selenium.find_element(By.XPATH, '//*[@id="wrapper"]/div/div/div/form/button')
        button.click()

        # 指定秒数待機(ページ遷移のため)
        time.sleep(3)

        # ページタイトルの検証
        self.assertEqual('日記一覧 | Private Diary', self.selenium.title)
    

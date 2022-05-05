from django.test import LiveServerTestCase
from django.urls import reverse_lazy
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class TestLogin(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver(executable_path='/Users/daiki/work/chromedriver')

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login(self):
        # ログインページを開く
        self.selenium.get('http://127.0.0.1:8000' + str(reverse_lazy('account_login')))

        # ログイン
        username_input = self.selenium.find_element(by=By.NAME, value='login')
        username_input.send_keys('test@example.com')
        password_input = self.selenium.find_element(by=By.NAME, value='password')
        password_input.send_keys('tst_psswd')
        self.selenium.find_element(by=By.CLASS_NAME, value='btn').click()

        # ページタイトルの検証
        self.assertEqual('日記一覧 | Private Diary', self.selenium.title)

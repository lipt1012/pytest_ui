# coding:utf-8
import pytest
import allure
import time
import sys
sys.path.append("../")  # 提升2级到项目根目录下
from config.config import *  # 从项目路径下导入
from public.common.read_excel import *  # 从项目路径下导入
from public.common.case_log import log_login_info  # 从项目路径下导入
from public.pages.login import Login
sys.path.append('..')
from config.config import *
sys.path.append('../')
from module.login_pages import  BaseCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options




class TestUserReg(BaseCase):    


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
           
    def test_01(self):
        case_data = get_test_data(self.data_list, 'test_01')
        self.send(case_data)


                                 
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    pytest.main()

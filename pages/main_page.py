import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class Main_page(Base):

    url = 'https://shoeslel.com/'

    #Locators

    for_him = '/html/body/header/div/div[2]/div/div/nav/ul/li[2]/a'
    main_word = '//h1[@class="title main-content__title"]'

    #Getters

    def get_for_him(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.for_him)))
    def get_main_word(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.main_word)))

    # Actions

    def click_for_him(self):
        self.get_for_him().click()
        print('Click select_product_1')

    # Methods

    def select_for_him(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_for_him()
        time.sleep(5)
        self.assert_word(self.get_main_word(), 'МУЖСКАЯ ОБУВЬ')

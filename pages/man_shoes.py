import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class Man_shoes(Base):

    #Locators

    type_shoes = "//form[@id='filter-form']/fieldset[2]"
    select_kedy = "//label[@data-id='kedy']"
    select_size = "//form[@id='filter-form']/fieldset[8]"
    size_43 = "//div[@id='filtergood-size']/div[11]"
    apply_button = "//*[contains(text(),'Применить')]"
    man_word = '//h1[@class="title main-content__title"]'


    #Getters

    def get_type_shoes(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.type_shoes)))
    def get_select_kedy(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.select_kedy)))
    def get_select_size(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.select_size)))
    def get_size_43(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.size_43)))
    def get_apply_button(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.apply_button)))
    def get_man_word(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.man_word)))

    # Actions

    def click_type_shoes(self):
        self.get_type_shoes().click()
        print('click_type_shoes')
    def click_select_kedy(self):
        self.get_select_kedy().click()
        print('click_select_kedy')
    def click_filtr_size(self):
        self.get_select_size().click()
        print('click_filtr_size')
    def click_size_selection(self):
        self.get_size_43().click()
        print('click_size_selection')
    def click_apply_filtr(self):
        self.get_apply_button().click()
        print('click_apply_filtr')

    # Methods

    def man_type(self):
        self.click_type_shoes()

    def type_kedy(self):
        self.click_select_kedy()

    def size_type(self):
        self.click_filtr_size()

    def kedy_size_43(self):
        self.click_size_selection()

    def apply(self):
        self.click_apply_filtr()
        time.sleep(4)
        self.assert_word(self.get_man_word(), 'МУЖСКИЕ КЕДЫ 43 РАЗМЕРА')


from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class Select_model(Base):

    #Locators

    select_product_1 = "//article[@data-id='1894']"
    select_size_product_1 = "//label[@for='basket-good_size-10306']"
    basket_select_product_1 = "//*[contains(text(),'В корзину')]"
    go_basket = "//div[@class='content']/div[1]/a[1]"
    select_model_word = "//h1[@class='title-grey']"

    #Getters

    def get_select_product_1(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.select_product_1)))
    def get_select_size_product_1(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.select_size_product_1)))
    def get_basket_select_product_1(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.basket_select_product_1)))
    def get_go_basket(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.go_basket)))
    def get_select_model_word(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.select_model_word)))

    # Actions

    def click_select_product_1(self):
        self.get_select_product_1().click()
        print('Click select_product_1')
    def click_select_size_product_1(self):
        self.get_select_size_product_1().click()
        print('Click select_size_product_1')
    def click_basket_select_product_1(self):
        self.get_basket_select_product_1().click()
        print('Click basket_select_product_1')
    def click_go_basket(self):
        self.get_go_basket().click()
        print('Click go_basket')

    # Methods

    def choice_select_product_1(self):
        self.click_select_product_1()
        self.assert_word(self.get_select_model_word(), 'Полуботинки, артикул 2181, цвет серый')
        print('Good Select product')

    def choice_size_product_1(self):
        self.click_select_size_product_1()

    def choice_basket_select_product_1(self):
        self.click_basket_select_product_1()

    def choice_click_go_basket(self):
        self.click_go_basket()


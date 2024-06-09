import time
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base

class Filling_basket(Base):

    #Locators

    name = "//input[@id='orderform-first_name']"
    last_name = "//input[@id='orderform-last_name']"
    email = "//input[@id='orderform-email']"
    phone = "//input[@id='orderform-phone']"
    locality = "//input[@id='orderform-locality']"
    locality_space = "//input[@id='orderform-locality']"
    delivery = "//label[@for='OrderForm[delivery_list][1]']"
    street = "//input[@id='orderform-street']"
    house = "//input[@id='orderform-house']"
    postcode = "//input[@id='orderform-postcode']"
    payment_online = "//label[@for='OrderForm[payment_method][1]']"
    button_payment = "//*[contains(text(),'Оплатить онлайн')]"
    price_basket = "//span[@class='table-cart__curprice']"
    size_basket = "//table[@class='table-attribute']/tbody/tr[3]/td[2]"
    color_basket = "//table[@class='table-attribute']/tbody/tr[2]/td[2]"
    model_basket = "//table[@class='table-attribute']/tbody/tr[1]/td[2]"
    #Getters

    def get_name(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.name)))
    def get_last_name(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.last_name)))
    def get_email(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.email)))
    def get_phone(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.phone)))
    def get_locality(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.locality)))
    def get_locality_space(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.locality_space)))
    def get_delivery(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.delivery)))
    def get_street(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.street)))
    def get_house(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.house)))
    def get_postcode(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.postcode)))
    def get_payment_online(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.payment_online)))
    def get_button_payment(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.button_payment)))
    def get_price_basket(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.price_basket)))
    def get_size_basket(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.size_basket)))
    def get_color_basket(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.color_basket)))
    def get_model_basket(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.model_basket)))

    # Actions

    def input_name(self):
        self.get_name().send_keys('Иван')
        print('ОК input_name')
    def input_last_name(self):
        self.get_last_name().send_keys('Иванов')
        print('ОК input_last_name')
    def input_email(self):
        self.get_email().send_keys('abc@ya.ru')
        print('ОК input_email')
    def input_phone(self):
        self.get_phone().send_keys('+79999999999')
        print('OK input_phone')
    def input_locality(self):
        self.get_locality().send_keys('Кировская обл')
        print('OK input_locality')
    def input_locality_space(self):
        self.get_locality_space().send_keys(' ')
        print('OK locality_space')
    def click_delivery(self):
        self.get_delivery().click()
        print('Click delivery')
    def input_street(self):
        self.get_street().send_keys('Советская')
        print('ОК input_street')
    def input_house(self):
        self.get_house().send_keys('1')
        print('ОК input_house')
    def input_postcode(self):
        self.get_postcode().send_keys('610000')
        print('ОК input_postcode')
    def click_payment_online(self):
        self.get_payment_online().click()
        print('Click payment_online')
    def click_payment(self):
        self.get_button_payment().click()
        print('Click payment')

    # Methods

    def check_filling_price(self):
        self.assert_word(self.get_price_basket(), '4 500.00 pуб.')
        print('Good basket price')
    def check_filling_size(self):
        self.assert_word(self.get_size_basket(), '43')
        print('Good basket size')
    def check_filling_color(self):
        self.assert_word(self.get_color_basket(), 'серый')
        print('Good basket color')
    def check_filling_model(self):
        self.assert_word(self.get_model_basket(), '2181')
        print('Good basket model')

    def name_user_1(self):
        self.input_name()

    def last_name_user_1(self):
        self.input_last_name()

    def email_user_1(self):
        self.input_email()

    def phone_user_1(self):
        self.input_phone()

    def locality_user_1(self):
        self.input_locality()
        time.sleep(5)
        self.get_locality().send_keys(Keys.RETURN)
        self.get_locality().send_keys('\n')
        time.sleep(2)
        self.get_locality().send_keys(' ')
        time.sleep(2)
        self.get_locality().send_keys(Keys.RETURN)

    def space(self):
        self.input_locality_space()
        time.sleep(2)
        self.get_locality_space().send_keys(Keys.RETURN)

    def click_select_delivery(self):
        self.click_delivery()

    def input_street_1(self):
        self.input_street()
        self.get_locality().send_keys(Keys.RETURN)
    def input_house_1(self):
        self.input_house()
        time.sleep(3)
        self.get_locality().send_keys(Keys.RETURN)
    def input_postcode_1(self):
        self.input_postcode()
    def select_click_payment_online(self):
        self.click_payment_online()
    def select_click_payment(self):
        self.click_payment()



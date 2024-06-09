import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.filling_basket import Filling_basket
from pages.main_page import Main_page
from pages.man_shoes import Man_shoes
from pages.select_model import Select_model
options = webdriver.ChromeOptions()

def test_select_for_him():
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    print('Start test 1')

    mp = Main_page(driver)
    mp.select_for_him()

    ms = Man_shoes(driver)
    ms.man_type()
    ms.type_kedy()

    driver.execute_script('window.scrollTo(0,500)')
    time.sleep(3)

    ms = Man_shoes(driver)
    ms.size_type()
    time.sleep(3)

    ms = Man_shoes(driver)
    ms.kedy_size_43()
    time.sleep(3)
    ms.apply()
    time.sleep(3)
    driver.execute_script('window.scrollTo(0,350)')

    sm = Select_model(driver)
    sm.choice_select_product_1()

    driver.execute_script('window.scrollTo(0,500)')
    time.sleep(3)

    sm = Select_model(driver)
    sm.choice_size_product_1()
    time.sleep(3)
    sm.choice_basket_select_product_1()
    time.sleep(3)

    sm = Select_model(driver)
    sm.choice_click_go_basket()

    fb = Filling_basket(driver)
    fb.name_user_1()
    fb.last_name_user_1()
    fb.email_user_1()
    fb.phone_user_1()
    fb.locality_user_1()

    driver.execute_script('window.scrollTo(0,600)')

    fb = Filling_basket(driver)
    fb.space()
    time.sleep(3)
    fb.check_filling_price()
    fb.check_filling_size()
    fb.check_filling_model()
    fb.check_filling_color()
    fb.click_select_delivery()
    driver.execute_script('window.scrollTo(0,800)')
    time.sleep(2)
    fb.input_street_1()
    time.sleep(2)
    fb.input_house_1()
    fb.input_postcode_1()
    time.sleep(3)
    fb.select_click_payment_online()

    driver.execute_script('window.scrollTo(0,1000)')
    time.sleep(3)
    fb.select_click_payment()
    print('Finish test 1')













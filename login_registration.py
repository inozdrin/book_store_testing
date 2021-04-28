# -- author: Igor Nozdrin --
# -- Created by Igor at 4/24/2021 --
# -- coding = "utf-8" ---

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()

# Jump on the site
driver.get('http://practice.automationtesting.in/')

# *************************************************************************************
#   Go to My Account menu
my_account_menu = driver.find_element_by_css_selector('li#menu-item-50>a')
my_account_menu.click()

# Registration Email
reg_email = driver.find_element_by_id('reg_email')
reg_email.send_keys('qwerty2@email.com')

#   Registration Password
# The password should be at least seven characters long.
# To make it stronger, use upper and lower case letters, numbers and symbols like ! " ? $ % ^ & ).
reg_password = driver.find_element_by_id('reg_password')
reg_password.send_keys('1Qaws102!!asdf')

#   Click Register Button

register_btn = driver.find_element_by_xpath("//p[@class='woocomerce-FormRow form-row']/input[3]")
register_btn.click()

time.sleep(30)
# ************************************************************************************
#   Close Driver
driver.close()

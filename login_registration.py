# -- author: Igor Nozdrin --
# -- Created by Igor at 4/24/2021 --
# -- coding = "utf-8" ---

from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def logout():
    if driver.current_url == 'http://practice.automationtesting.in/my-account/':
        driver.find_element_by_css_selector('.woocommerce-MyAccount-navigation-link--customer-logout>a').click()
        print(f'We were on My Account Page and Logged out')
    else:
        driver.find_element_by_css_selector('li#menu-item-50>a').click()
        driver.find_element_by_css_selector('.woocommerce-MyAccount-navigation-link--customer-logout>a').click()
        print(f'We moved to My Account Page and Logged out')


# *****     Registration Test      *****
# ******************************************************************************

driver = webdriver.Chrome()
driver.maximize_window()

# *****************************************************************************
# Close Chrome Settings Tab
current_window = driver.window_handles[1]
chrome_sett_tab = driver.window_handles[0]
driver.switch_to.window(chrome_sett_tab)
driver.close()
driver.switch_to.window(current_window)

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

# *****************************************************************************
#   Close Driver
driver.close()
# ******************************************************************************
# Registration Done
# ******************************************************************************



# *****     Login Test      *****
# ******************************************************************************
email = 'qwerty2@email.com'
password = '1Qaws102!!asdf'

driver = webdriver.Chrome()
driver.maximize_window()

# *****************************************************************************
# Close Chrome Settings Tab
current_window = driver.window_handles[1]
chrome_sett_tab = driver.window_handles[0]
driver.switch_to.window(chrome_sett_tab)
driver.close()
driver.switch_to.window(current_window)

# ******************************************************************************
# Jump on the site
driver.get('http://practice.automationtesting.in/')
driver.implicitly_wait(5)

#   Go to My Account menu
my_account_menu = driver.find_element_by_css_selector('li#menu-item-50>a')
my_account_menu.click()

# Login Email

login_email = driver.find_element_by_id('username')
login_email.send_keys(email)

#   Login Password
# The password should be at least seven characters long.
# To make it stronger, use upper and lower case letters, numbers and symbols like ! " ? $ % ^ & ).
login_password = driver.find_element_by_id('password')
login_password.send_keys(password)

#   Click Login Button
login_btn = driver.find_element_by_xpath("//p[@class='form-row']/input[3]")
login_btn.click()

#   Check the existing Logout element
check_logout = WebDriverWait(driver, 20).until(
    EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, ".woocommerce-MyAccount-navigation-link--customer-logout>a"), 'Logout'))

if check_logout is True:
    print('The Login element has been found!')
else:
    print('There is no LOGOUT element!')

#time.sleep(10)
# ************************************************************************************
#   Close Driver
driver.close()

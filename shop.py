# -- author: Igor Nozdrin --
# -- Created by Igor at 4/24/2021 --
# -- coding = "utf-8" ---
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


# *****************************************************************************
# Close Chrome Settings Tab
# current_window = driver.window_handles[1]
# chrome_sett_tab = driver.window_handles[0]
# driver.switch_to.window(chrome_sett_tab)
# driver.close()
# driver.switch_to.window(current_window)


# *****************************************************************************
# Functions block

# Check How many windows are open
def check_tabs():
    if len(driver.window_handles) > 1:
        current_window = driver.window_handles[1]
        chrome_sett_tab = driver.window_handles[0]
        driver.switch_to.window(chrome_sett_tab)
        driver.close()
        driver.switch_to.window(current_window)
    else:
        pass


# Switch to Shop
def go_to_shop():
    shop_menu = driver.find_element_by_css_selector('#menu-item-40>a')
    shop_menu.click()


# Fill ouy Login form
def login_form(email, password):  # login form fill out
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


# Log out
def logout():
    if driver.current_url == 'http://practice.automationtesting.in/my-account/':
        driver.find_element_by_css_selector('.woocommerce-MyAccount-navigation-link--customer-logout>a').click()
        print(f'We were on My Account Page and Logged out')
    else:
        driver.find_element_by_css_selector('li#menu-item-50>a').click()
        driver.find_element_by_css_selector('.woocommerce-MyAccount-navigation-link--customer-logout>a').click()
        print(f'We moved to My Account Page and Logged out')


# Prepare Chrome browser
driver = webdriver.Chrome()
driver.maximize_window()

# Check how many tabs
check_tabs()

# ******************************************************************************
# Here is log in information
email = 'qwerty2@email.com'
password = '1Qaws102!!asdf'
# ******************************************************************************
# Jump on site
driver.get('http://practice.automationtesting.in/')
driver.implicitly_wait(5)

#   Go to My Account menu
# my_account_menu = driver.find_element_by_css_selector('li#menu-item-50>a')
# my_account_menu.click()

# Login Email

# login_email = driver.find_element_by_id('username')
# login_email.send_keys('qwerty2@email.com')

#   Login Password
# The password should be at least seven characters long.
# To make it stronger, use upper and lower case letters, numbers and symbols like ! " ? $ % ^ & ).
# login_password = driver.find_element_by_id('password')
# login_password.send_keys('1Qaws102!!asdf')
# time.sleep(2)

#   Click Login Button
# login_btn = driver.find_element_by_xpath("//p[@class='form-row']/input[3]")
# login_btn.click()

# *****************************************************************************
#   Section 1 Shop: Show item page

#   Log in
login_form(email, password)

#    Click Shop button
# shop_menu = driver.find_element_by_css_selector('#menu-item-40>a')
# shop_menu.click()
go_to_shop()

# Click on HTML Forms book
forms_book = driver.find_element_by_css_selector('.post-181>a')
forms_book.click()

# Check Book Title

book_title = driver.find_element_by_css_selector('.product_title')
print(book_title)
book_title_text = book_title.text
assert book_title_text == "HTML5 Forms"
print(f'The title of this book is: {book_title_text}')

logout()
print('*****We finished the First test*****')
# time.sleep(5)

# *****************************************************************************
#   Section 2 Shop: items quantity in category

# Log in
login_form(email, password)

#   return to the shop page

# shop_menu = driver.find_element_by_css_selector('#menu-item-40>a')
# shop_menu.click()
go_to_shop()

#   Go to HTML block
html_block_link = driver.find_element_by_css_selector('li.cat-item-19>a')
html_block_link.click()

#   Test How many items shown
html_numbers1 = driver.find_element_by_css_selector('li.cat-item-19>span')
how_many_items = html_numbers1.text
print(f'There are {how_many_items} items on this page')

# Test How many items presented on the page
items_present = driver.find_elements_by_css_selector('ul.products>li')
count_items = len(items_present)
print(f'There are {count_items} on this page')
assert how_many_items == '(3)'
assert count_items == 3

#   Log out
logout()
print('*****We finished the Second test*****')

# *****************************************************************************
#   Section 3 Shop: Sorting items

# Log in
login_form(email, password)

# Return to shop main page
go_to_shop()

#   Check the default option is selected
sort_selector_option = driver.find_element_by_xpath('//select/option[1]')
assert sort_selector_option.get_attribute('value') == 'menu_order'
print(f'Select element attribute Value: {sort_selector_option.get_attribute("value")}')

# Sort from High to low
sort_selector = driver.find_element_by_class_name('orderby')
select = Select(sort_selector)
select.select_by_value('price-desc')

#   Check high to low sorting is selected

selected_option = driver.find_element_by_css_selector('.orderby>option[selected="selected"]')
sort_selector_value = selected_option.get_attribute('value')
assert sort_selector_value == 'price-desc'
print(sort_selector_value)

#   Log out
logout()
print('*****We finished the Third test*****')
# *****************************************************************************
#   Section 4 Shop: Showing items, discounts

# Log in
login_form(email, password)
go_to_shop()

#   Android book click

android_book = driver.find_element_by_css_selector('.post-169>a')
android_book.click()

#   Check Old price
old_price = driver.find_element_by_css_selector('p.price>del>span.woocommerce-Price-amount.amount')

print(f'The old price: {old_price.text}')
assert old_price.text == '₹600.00'

#  Check New price
new_price = driver.find_element_by_css_selector('p.price>ins>span.woocommerce-Price-amount.amount')
print(f'The new price: {new_price.text}')
assert new_price.text == '₹450.00'

# Click Book image and add Explicit Wait
# element_check = WebDriverWait(driver, 20 ).until(EC.element_to_be_selected(some_element))
# picture = driver.find_element_by_css_selector('.images>a')
# picture.click()
# picture_win = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'fullResImage')))
picture_win = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.images>a')))
picture_win.click()

close_pic = driver.find_element_by_class_name('pp_close')
close_pic.click()
# Click on hidden link
# hidden_arrow = driver.find_element_by_class_name('pp_arrow_next')
# hidden_arrow.click()


#   Close Pop Up window with picture
# close_btn = driver.find_element_by_class_name('pp_close')
# close_btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, 'pp_close')))
# close_btn.click()
logout()
print('*****We finished the Fourth test*****')
# *****************************************************************************
#   Section 4 Shop: Showing items, discounts

#   Return to shop
go_to_shop()

print(driver.current_url)

time.sleep(10)
# *****************************************************************************
#   Close Driver
driver.close()

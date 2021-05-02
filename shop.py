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
# Functions block

# Check How many windows are open and Close Chrome Settings Tab
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
    time.sleep(10)
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


# ******************************************************************************
# Here is log in information
email = 'qwerty2@email.com'
password = '1Qaws102!!asdf'
# ******************************************************************************
driver = webdriver.Chrome()
driver.maximize_window()
check_tabs()
# Jump on site
driver.get('http://practice.automationtesting.in/')
driver.implicitly_wait(5)

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
driver.close()

# *****************************************************************************
#   Section 2 Shop: items quantity in category

driver = webdriver.Chrome()
driver.maximize_window()
check_tabs()
# Jump on site
driver.get('http://practice.automationtesting.in/')
driver.implicitly_wait(5)

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
driver.close()

# *****************************************************************************
#   Section 3 Shop: Sorting items
driver = webdriver.Chrome()
driver.maximize_window()
check_tabs()
# Jump on site
driver.get('http://practice.automationtesting.in/')
driver.implicitly_wait(5)

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
driver.close()
# *****************************************************************************
#   Section 4 Shop: Showing items, discounts
driver = webdriver.Chrome()
driver.maximize_window()
check_tabs()
# Jump on site
driver.get('http://practice.automationtesting.in/')
driver.implicitly_wait(5)

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
picture_win = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.images>a')))
picture_win.click()
#   Close Pop Up window with picture
close_pic = driver.find_element_by_class_name('pp_close')
close_pic.click()

logout()
print('*****We finished the Fourth test*****')
driver.close()

# *****************************************************************************
#   Section 5 Shop: Check price in the Basket

# Prepare Chrome browser
driver = webdriver.Chrome()
driver.maximize_window()
# Check how many tabs
check_tabs()
# Jump on site
driver.get('http://practice.automationtesting.in/')
driver.implicitly_wait(5)

#   Return to shop
go_to_shop()

# Click Add to Basket button
add_basket_btn = driver.find_element_by_css_selector('li.post-182>a+a')
add_basket_btn.click()
time.sleep(5)

#   Check How many items in Basket
items_basket = driver.find_element_by_css_selector('span.cartcontents')
items_basket_text = items_basket.text
time.sleep(5)
print(items_basket.text)
print(items_basket_text)

assert items_basket_text == "1 Item"
if items_basket_text == '1 Item':
    print(f"There is/are {items_basket_text} in the Basket")
else:
    print(f"Something is going wrong!")

#   Check item price in Basket
amount = driver.find_element_by_css_selector('span.amount')
amount_text = amount.text
assert amount_text == '₹180.00'
if amount_text == '₹180.00':
    print(f"The price is {amount_text}.")
else:
    print(f"Something is going wrong!")

#   Go to Basket
go_basket = driver.find_element_by_class_name("wpmenucart-contents")
go_basket.click()

#   Check Subtotal

sub_amount = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.product-subtotal>span'), '₹180.00'))
print(f'Subtotal Presence - {sub_amount}')
if sub_amount is True:
    print('Subtotal is OK')
else:
    print('Subtotal - something wrong')

#  Check Total amount
tot_amount = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'tr.order-total>td>strong>span'), '₹189.00'))
print(f'Total Presence - {tot_amount}')
if tot_amount is True:
    print('Total is OK')
else:
    print('Total - something wrong')
time.sleep(5)
# *****************************************************************************
#   Close Driver
driver.close()

# *****************************************************************************
#   Section 6 Shop: Work in the Basket

# Prepare Chrome browser
driver = webdriver.Chrome()
driver.maximize_window()
# Check how many tabs
check_tabs()

# Jump on site
driver.get('http://practice.automationtesting.in/')
driver.implicitly_wait(5)

#   Return to shop
go_to_shop()

#   Scroll down 300 pxls
driver.execute_script('window.scrollBy(0,300);')

# Click Add to Basket button HTML5 WebApp Development and JS Data Structures and Algorithm
add_basketHTML_btn = driver.find_element_by_css_selector('li.post-182>a+a')
add_basketHTML_btn.click()

time.sleep(5)

add_basketJS_btn = driver.find_element_by_css_selector('li.post-180>a+a')
add_basketJS_btn.click()

# time.sleep(5)

#   Go to Basket
go_basket = driver.find_element_by_class_name("wpmenucart-contents")
go_basket.click()

time.sleep(5)

#   Delete the first book
first_del_btn = driver.find_element_by_xpath("//tr[@class='cart_item']/td/a")
first_del_btn.click()

#   Click Undo
undo_link = driver.find_element_by_css_selector('.woocommerce-message>a')
undo_link.click()
time.sleep(5)
#   Change  JS book Qty to 3

qty_JS_field = driver.find_element_by_xpath("//tbody/tr[1]/td[@class='product-quantity']/div/input")

qty_JS_field.clear()
time.sleep(2)
qty_JS_field.send_keys(3)

#   Click Update Basket
update_btn = driver.find_element_by_css_selector('td>input.button')
update_btn.click()

qty_JS_field = driver.find_element_by_xpath(
    "//tbody/tr[1]/td[@class='product-quantity']/div/input").get_property('value')
print(qty_JS_field)
assert qty_JS_field == '3'
time.sleep(5)
#   Click Apply Coupon button
app_coupon_btn = driver.find_element_by_css_selector(".coupon>input.button")
app_coupon_btn.click()

#   Check error message
err_message = driver.find_element_by_css_selector('.woocommerce-error>li')
err_msg_text = err_message.text
assert err_msg_text == 'Please enter a coupon code.'
if err_msg_text == 'Please enter a coupon code.':
    print("The error msg is: Please enter a coupon code.")
else:
    print("The error msg is: Something else.")

time.sleep(30)
# *****************************************************************************
#   Close Driver
driver.close()

# *****************************************************************************
#   Section 7 Shop: Purchase

# Prepare Chrome browser
driver = webdriver.Chrome()
driver.maximize_window()
# Check how many tabs
check_tabs()

# Jump on site
driver.get('http://practice.automationtesting.in/')
driver.implicitly_wait(5)

#   Return to shop
go_to_shop()

#   Scroll down 300 pxls
driver.execute_script('window.scrollBy(0,300);')

# Click Add to Basket button
add_basketHTML_btn = driver.find_element_by_css_selector('li.post-182>a+a')
add_basketHTML_btn.click()
time.sleep(5)

#   Go to Basket
go_basket = driver.find_element_by_class_name("wpmenucart-contents")
go_basket.click()

#   Click Button Proceed To checkpoint
# proc_to_check_btn = driver.find_element_by_css_selector('.wc-proceed-to-checkout>a')
proc_to_check_btn = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '.wc-proceed-to-checkout>a')))
proc_to_check_btn.click()

#   Fill First name field
first_name_tbox = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, 'billing_first_name')))
# first_name_tbox = driver.find_element_by_id('billing_first_name')
first_name_tbox.send_keys('Vasia')

#   Fill Last name field
last_name_tbox = driver.find_element_by_id('billing_last_name')
last_name_tbox.send_keys('Pupkin')

#   Fill Email field
billing_email_tbox = driver.find_element_by_id('billing_email')
billing_email_tbox.send_keys('adfdsfds@sadfsaf.com')

#   Fill Phone field
billing_phone_tbox = driver.find_element_by_id('billing_phone')
billing_phone_tbox.send_keys('123456789')

#   Fill Phone field
billing_phone_tbox = driver.find_element_by_id('billing_phone')
billing_phone_tbox.send_keys('123456789')

#   Country Selector
country_selector = driver.find_element_by_css_selector('#s2id_billing_country>a')
country_selector.click()
# нажать на селектор - > ввести название в поле ввода - > нажать на вариант который отобразится ниже ввода
# id="select2-result-label-1175"
country_entry = driver.find_element_by_id("s2id_autogen1_search")
country_entry.send_keys('United Kingdom (UK)')
time.sleep(5)
# Click on found country
# found_sel_country = driver.find_element_by_id("select2-result-label-2453")
# found_sel_country = driver.find_elements_by_class_name("select2-match")
found_sel_country = driver.find_element_by_id("select2-results-1")

found_sel_country.click()

#   Fill Address field
addr_tbox = driver.find_element_by_css_selector('input#billing_address_1')
addr_tbox.send_keys('A4, London WC2N 5DU, UK')

#   Fill Postal/ZIP
postal_tbox = driver.find_element_by_id('billing_postcode')
postal_tbox.send_keys('WC2N 5DU')

#   Fill Town/City
town_tbox = driver.find_element_by_id('billing_city')
town_tbox.send_keys('London')

#   Scroll down 300 pxls
driver.execute_script('window.scrollBy(0,300);')
time.sleep(5)

#   Check payment
chk_payment_rbtn = driver.find_element_by_id('payment_method_cheque')
chk_payment_rbtn.click()

#   Click Place Order
place_order_btn = driver.find_element_by_id('place_order')
place_order_btn.click()

time.sleep(10)
#   Check Order
# thank_message = driver.find_elements_by_class_name('.woocommerce-thankyou-order-received')
thank_message = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'woocommerce-thankyou-order-received')))
print(thank_message)
if thank_message:
    print(f'We made the order')
else:
    print(f'Something is not going right')

chk_payment = WebDriverWait(driver, 20).until(
    EC.text_to_be_present_in_element((
        By.XPATH, "//table[@class='shop_table order_details']/tfoot/tr[3]/td"), 'Check Payments'))
if chk_payment:
    print(f'Check payment is OK')
else:
    print(f'Something is not going right')

time.sleep(10)
# *****************************************************************************
#   Close Driver
driver.close()





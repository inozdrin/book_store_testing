# -- author: Igor Nozdrin --
# -- Created by Igor at 4/24/2021 --
# -- coding = "utf-8" ---
from selenium import webdriver
#import time

def check_tabs():   # Checking if Chrome Settings  Tab opens when browser starts
    if len(driver.window_handles) > 1:
        current_window = driver.window_handles[1]
        chrome_sett_tab = driver.window_handles[0]
        driver.switch_to.window(chrome_sett_tab)
        driver.close()
        driver.switch_to.window(current_window)
    else:
        pass


driver = webdriver.Chrome()
driver.maximize_window()

check_tabs()
# Jump on the site
driver.get('http://practice.automationtesting.in/')

# *****************************************************************************
#   Scroll down 600 pxls
driver.execute_script('window.scrollBy(0,600);')

#   Click on Rubi READ MORE button
read_more_button = driver.find_element_by_css_selector('a.button')
read_more_button.click()

#    Click on Review Tab
review_tab = driver.find_element_by_css_selector('li.reviews_tab>a')
review_tab.click()

#   Click 5 star
five_star = driver.find_element_by_css_selector('a.star-5')
five_star.click()

#   Leave comment
tbox_comment = driver.find_element_by_id('comment')
tbox_comment.send_keys('Nice book!')

# Name text box
tbox_name = driver.find_element_by_id('author')
tbox_name.send_keys('Vasia Pupkin')

#   Email
tbox_email = driver.find_element_by_id('email')
tbox_email.send_keys('vasiapupkin@qwerty.com')

#   Click Submit

submit_btn = driver.find_element_by_id('submit')
submit_btn.click()


# *****************************************************************************
#   Close Driver
driver.close()


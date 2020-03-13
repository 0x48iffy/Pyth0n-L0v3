
from selenium import webdriver


browser = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')

#open link on browser
url="https://facebook.com"
browser.get(url)

#fill username:
browser.find_element_by_xpath('//*[@id="email"]').send_keys('username')

#fill pass
browser.find_element_by_name('pass').send_keys('passs')

#click on button

browser.find_element_by_id('loginbutton').click()
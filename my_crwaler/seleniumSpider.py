from selenium import webdriver
from scrapy import selector
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
path = 'D:/selenium/chromedriver.exe'
chrome_options.add_experimental_option("prefs", prefs)
browser = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)

browser.get('http://www.ttmeiju.vip/meiju/House.of.Cards.html')
#browser.get('http://www.51cto.com/')
elems = browser.find_element_by_css_selector(".seasonitem").find_elements_by_xpath('//h3')


for elem in elems:
    if elem.get_attribute('onclick'):
        elem.click()

source = browser.page_source()

browser.close()

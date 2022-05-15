from selenium import webdriver
import webbrowser
driver = webdriver.Chrome()
url1 = 'https://github.com/login'
driver.get(url1)
button = driver.find_element_by_class_name('btn btn-primary btn-block js-sign-in-button')
button.click
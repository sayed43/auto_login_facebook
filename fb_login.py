from selenium import webdriver
from selenium import*
driver=webdriver.Chrome("G:\\chromedriver")

driver.get("https://www.facebook.com")

user=input("enter your phone or email: ")
password=input("enter your password: ")

email_field=driver.find_element_by_id("email")

email_field.send_keys(user)

pass_field=driver.find_element_by_id("pass")
pass_field.send_keys(password)

login_btn=driver.find_element_by_id("u_0_b")

login_btn.submit()


driver.find_elements_by_class_name("_1mf _1mj").send_keys("gello")


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
import urllib2 
import pdb
import time
import csv
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("http://flaky.voylla.com/mens-jewellery/mens-pendants")

#if driver.find_element_by_class_name('four0four'):
#	print "Error 500: Order Fail"

#else:
time.sleep(5)
driver.find_element_by_class_name("buy_btn_solr").click();


time.sleep(3)
driver.find_element_by_class_name("checkout_cart_div").click();

############################# Redirected to Checkout Page#####################################################################


select = Select(driver.find_element_by_id('salutation'))
select.select_by_value('Mr.')


driver.find_element_by_id("order_ship_address_attributes_firstname").send_keys("sudo");
driver.find_element_by_id("order_ship_address_attributes_lastname").send_keys("party");
driver.find_element_by_id("order_email").send_keys("sudoparty@gmail.com");
driver.find_element_by_id("order_ship_address_attributes_zipcode").send_keys("999999");
driver.find_element_by_id("order_ship_address_attributes_address").send_keys("Abc");

driver.find_element_by_id("order_ship_address_attributes_landmark").send_keys("QA");
#print "QA"
select = Select(driver.find_element_by_id('order_ship_address_attributes_state_id'))
select.select_by_value('1061493614')
#print "Rajasthan"
driver.find_element_by_id("order_ship_address_attributes_city").send_keys("Jaipur");
#print "Jaipur"

driver.find_element_by_id("order_ship_address_attributes_phone").send_keys("9828092692");
#print "9828092692"
time.sleep(5)

######  Mousehover Change to Buy NOw or Never#################################################################################
elm_Men_Menu = driver.find_element_by_class_name('voylla')
builder = ActionChains(driver)
builder.move_to_element(elm_Men_Menu).perform()
time.sleep(6)
#print "Proceed"

######## Click on Proceed to Payment ###########################################################################################	

driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/div/div[2]/div[1]/form/div[2]/div[2]/div/button").click();

driver.find_element_by_id("order_payment_via_cod").click();
#driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/form/input[2]").click();
#driver.find_element_by_class_name("enter_code").send_keys("aly0v")

######Print Order Id########################################################################################################
elem = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div[3]/div[2]")
print elem.text
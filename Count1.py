from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import pdb
import urllib2 
import smtplib

driver = webdriver.Firefox()
driver.maximize_window()
#pdb.set_trace()
driver.get("http://www.voylla.com/jewellery")
#pdb.set_trace()
#driver.maximize_window()
elem = driver.find_element_by_class_name('total_products_info')
#pdb.set_trace()
#driver.execute_script("return arguments[0].scrollIntoView();", element)
print elem.text
sender = 'siddharth.mehta@voylla.com'
receivers = ['sidmehta07@gmail.com']
message = """From: Voylla Listing <siddharh.mehta@voylla.com>
 


Today's Product Count is
%s

 """%(elem.text)

try:
	smtpObj = smtplib.SMTP('smtp.gmail.com:587')
	smtpObj.ehlo()
	smtpObj.starttls()
	smtpObj.login("siddharth.mehta@voylla.com", "siddharth@voylla.com")
	smtpObj.sendmail(sender, receivers, message)         
	smtpObj.quit()
	print "Successfully sent email"
except: 
	print "Error: unable to send email"	
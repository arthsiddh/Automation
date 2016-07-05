from bs4 import BeautifulSoup
import pdb
import urllib2 
import pkgutil 
import csv
import smtplib
tag = {}
Fitag = {}

with open("C:\Users\Siddharth\Desktop\Raw.csv") as forder_lines:
	#pdb.set_trace()
	reader = csv.DictReader(forder_lines)
	for row in reader:
	#for i in url:
		url = urllib2.urlopen(row['url'])
		content = url.read()
		soup = BeautifulSoup(content, "html.parser")
		result = soup.find(attrs={'class':'four0four'})
		if soup.find(attrs={'class':'four0four'}):
		# 	print (soup.find(attrs={'class':'four0four'}))
			tag[row['url']] = soup.find(attrs={'class':'four0four'})
		# 
		#  #   tag[row['url']] = No Error
		#   	sender = 'siddharth.mehta@voylla.com'
		#   	receivers = ['sidmehta07@gmail.com']
		#   	message = """From: Voylla Listing <siddharh.mehta@voylla.com>
				 


		#  	H1 Tags are
		#  	%s

		#   		"""%(tag)

		#  	try:
		# 		smtpObj = smtplib.SMTP('smtp.gmail.com:587')
		# 		smtpObj.ehlo()
		# 		smtpObj.starttls()
		# 		smtpObj.login("siddharth.mehta@voylla.com", "siddharth@voylla.com")
		# 		smtpObj.sendmail(sender, receivers, message)         
		# 		smtpObj.quit()
		#  		print "Successfully sent email"
		#  	except: 
		# 	 print "Error: unable to send email"	
		else:
			tag[row['url']] ='Links Check: No Error Found'
			
#			 
			
		print '============================'
######### Sending Mail for class:four0four ########################### 
	sender = 'siddharth.mehta@voylla.com'
	receivers = ['tech@voylla.com',]
	message = """From: Voylla Listing <siddharh.mehta@voylla.com>
			 


	Links Checked: No Error
	%s

		"""%(tag)

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
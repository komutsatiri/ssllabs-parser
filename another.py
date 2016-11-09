import lxml.html as LH
import schedule
import requests
import time
import os

WARNING = '\033[93m'
ENDC = '\033[0m'
FAIL = '\033[91m'
worst_list = '//div[@class="box boxStyleRight"]//div/a'
heartbleed='//td/*[contains(text(), "Heartbleed (vulnerability)")]/parent::td/following-sibling::td/* | //td[contains(text(), "Heartbleed (vulnerability)")]/following-sibling::td'
worst_page='https://www.ssllabs.com/ssltest/'

def get_list():
	os.system('clear')
	print "Liste aliniyor..."
	worst_response = requests.get(worst_page)
	worst_tree = LH.fromstring(worst_response.content)

	for atag in worst_tree.xpath(worst_list):
		details_response = requests.get(worst_page + atag.attrib['href'])
		details_tree = LH.fromstring(details_response.content)

		for vuln in details_tree.xpath(heartbleed):
			if vuln.text_content().startswith('Yes'):
				print WARNING + worst_page + atag.attrib['href'] + ENDC
			elif  vuln.text_content().startswith('No'):
				print worst_page + atag.attrib['href']
 			else:
				print FAIL + worst_page + atag.attrib['href'] + ENDC
			

schedule.every(11).seconds.do(get_list)

while 1:
	schedule.run_pending()
	time.sleep(1)
			
			
			


		

	
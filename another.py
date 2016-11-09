import lxml.html as LH
import requests

heartbleed='//table[@class = "reportTable"]/descendant::td/*[contains(text(), "Heartbleed (vulnerability)")]/parent::td/following-sibling::td/* | //table[@class = "reportTable"]/descendant::td[contains(text(), "Heartbleed (vulnerability)")]/following-sibling::td'
worst_page='https://www.ssllabs.com/ssltest/'

worst_response = requests.get(worst_page)
worst_tree = LH.fromstring(worst_response.content)

for atag in worst_tree.xpath('//div[@class="box boxStyleRight"]//div/a'):
	print(atag.attrib['href'], atag.text_content())
	details_response = requests.get(worst_page + atag.attrib['href'])
	details_tree = LH.fromstring(details_response.content)

	for vuln in details_tree.xpath(heartbleed):
		print vuln.text_content()
		

	
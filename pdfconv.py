import pdfkit
from time import sleep

urls = open('inputurls.txt', 'r')
url = urls.readlines()
for url in url:
	try:
		options = {
    			'custom-header': [('User-Agent', 'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36')],
				'enable-local-file-access':''
				}
		name = url.strip().split('/')[-2]
		pdf = pdfkit.from_url(url.strip(),f'{name}.pdf',options=options)
		sleep(2)
	except:
		pass
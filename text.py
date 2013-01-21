import mechanize
import cookielib
from BeautifulSoup import BeautifulSoup


class Base:
	URL_1 = 'http://icms.cc-courts.org/iotw/civil/default.asp'
	URL_2 = 'http://icms.cc-courts.org/iotw/logon.asp'
	URL_4 = 'http://icms.cc-courts.org/iotw/CIVIL/default.asp'
	
	print 'dd'
	
	
	br = mechanize.Browser(factory=mechanize.RobustFactory())
	br.set_handle_redirect(True)
	br.set_handle_referer(True)
	
	cj = cookielib.LWPCookieJar()
	br.set_cookiejar(cj)
	br.addheaders = [	('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1'),
						('Content-type', 'application/x-www-form-urlencoded; charset=UTF-8'),
						('Accept',	'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
						('Accept-Encoding','gzip, deflate'),
						('Accept-Language','en-US,en;q=0.5'),
						('Connection',	'keep-alive'),
						('Host','icms.cc-courts.org'),
					
					]
	
	br.open(URL_1)
	br.form = list(br.forms())[0]
	br.submit()
	
	br.form = list(br.forms())[0]
	br.submit()
	br.response()
	
	
	br.form = list(br.forms())[0]
	br.submit(name='search', label='Case Number Search')
	#response = br.response()
	#headers = response.info() 
	#headers["Content-type"] = "application/x-www-form-urlencoded"
	#response.set_data(response.get_data())
	#br.set_response(response)
	br.response()
	
	br.form = list(br.forms())[0]  # if not using mechanize.RobustFactory(), list index out of range is thrown here
	print len(list(br.forms()))
	#br.form['casetype'][0]= "A"
	br.form['casenumber']="MSC12-01331"
	br.submit(name='name1', label='Search')
	
	print br.response().read()
	
	
import mechanize
import cookielib
from BeautifulSoup import BeautifulSoup

class Base:

    URL_1 = 'http://icms.cc-courts.org/iotw/civil/default.asp'
    URL_2 = 'http://icms.cc-courts.org/iotw/logon.asp'
    URL_4 = 'http://icms.cc-courts.org/iotw/CIVIL/default.asp'        
    
    # Browser
    br = mechanize.Browser()

    # Cookie Jar
    cj = cookielib.LWPCookieJar()
    br.set_cookiejar(cj)


    # User-Agent (this is cheating, ok?)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
    r = br.open(URL_1)
    br.form = list(br.forms())[0]
    br.submit()
    br.form = list(br.forms())[0]
    br.submit()
    br.response().read()
   
    
    
    br.form = list(br.forms())[0]
    #print br.response().read() 
    #br.form.set_all_readonly(False)
    #br.form["courtcode"] ="0"
    br.form = list(br.forms())[0]
    
    br.submit(name='search', label='Case Number Search')
    
   
    
    #br.response().read()
    
    soup = BeautifulSoup( br.get_data())
    
    #br.set_data()
    br.set_response(soup.prettify())
    '''
    br.select_form(name='main')
    '''
    #br.form = list(br.forms())
    #br.select_form(nr=0)
    br.form = list(br.forms())[0]
    br.form['casetype']= "A"
    br.form['casenumber']="MSC12-01331"
    br.submit(name='name1', label='Search')
    print br.response().read()
    
    
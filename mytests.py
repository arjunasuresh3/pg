import lxml.html
import urllib, pprint

url = 'http://www.pgguest.com/pgguest/default.aspx'

suburl = 'http://www.pgguest.com/pgguest/'

root = lxml.html.parse(url).getroot()

lefttab = root.xpath('//table[@id="tabLink"]')

for asd in lefttab[0]:
    #import pdb;pdb.set_trace()
    pprint.pprint(suburl + asd[0][0][0].values()[0])



import lxml.html
import urllib, pprint

url = 'http://www.pgguest.com/pgguest/default.aspx'
suburl = 'http://www.pgguest.com/pgguest/'
root = lxml.html.parse(url).getroot()
lefttab = root.xpath('//table[@id="tabLink"]')
area_wise = {}

for area in lefttab[0]:
    print "\n\n\n"
    pprint.pprint(suburl + area[0][0][0].values()[0])
    area_url = suburl + area[0][0][0].values()[0]
    area_root = lxml.html.parse(area_url).getroot()    
    pgs = area_root.xpath('//table[@id="tabDisplay"]')
    area_wise[area[0][0].text_content()] = []
    for pg in pgs[0]:
        append_dict = {}
        append_dict["name"] = pg[0][0][0][0][0].text_content()
        append_dict["address"] = pg[0][0][0][0][1].text_content()
        append_dict["des"] = pg[0][0][0][1][0].text_content()
        append_dict["phone"] = pg[0][0][0][2][0].text_content()
        pprint.pprint(append_dict)
        print "\n\n\n"
        area_wise[area[0][0].text_content()].append(append_dict)

pprint.pprint(area_wise)

import scraperwiki

# max 1891157
for crno in range(1, 10):
    crnostr = "%07d" % crno
    baseurl = "https://www.mobile-cr.gov.hk/mob/cps_criteria.do?queryCRNO="
    html = scraperwiki.scrape(baseurl + crnostr).decode('utf-8')

    import lxml.html           
    root = lxml.html.fromstring(html) # , encoding="utf-8")

    tds = root.cssselect("tr td tr td")
    namestds = root.cssselect("td.data")   

    if tds == []:
        pass
    else:
        print tds[2].text_content().encode('utf-8')
        names = {}
        for namesno in range(len(namestds)):
            names["Name" + str(namesno)] = namestds[namesno].text_content().encode('utf-8')
        data = {
        'cr' : tds[1].text_content().encode('utf-8'),
        'English Company Name' : tds[2].text_content().encode('utf-8').rsplit('\r')[1].lstrip('\n\t'),
        'Chinese Company Name' : tds[2].text_content().encode('utf-8').rpartition('\r')[2].lstrip('\r\n\t'),
        'Company Type' : tds[4].text_content().encode('utf-8')[:-1],
        'Date of incorporation' : tds[6].text_content().encode('utf-8'),
        'Company status' : tds[8].text_content().encode('utf-8')[:-1],
        'Active status' : tds[10].text_content().encode('utf-8')[:-1],
        'Remarks' : tds[11].text_content().encode('utf-8')[16:],
        'Winding up mode' : tds[13].text_content().encode('utf-8')[:-1],
        'Date of Dissolution' : tds[15].text_content().encode('utf-8'),
        'Register of Charges' : tds[17].text_content().encode('utf-8')[:-1],
        'Important Note' : tds[18].text_content().encode('utf-8')[15:].lstrip('\r\n\t'),
        'Name History' : names
        }
        

    scraperwiki.sqlite.save(unique_keys=['cr'], data=data)
        

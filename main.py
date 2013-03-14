import urllib2

for num in range(10000,18000):                  # change values here to get more pictures 
    url = "http://218.248.47.9/sis/control/img/P12612.JPG?imgId=P" 
    nurl = url + str(num)
    try:
        web_raw_results = urllib2.urlopen(nurl)
        
    except urllib2.HTTPError, detail:
        if detail.errno == 500:
            nurl = url + str(num+1)        
       
    else:
        urlContent = urllib2.urlopen(nurl).read()	  
        fileName = "pic"
        fileName = fileName + str(num) + ".jpeg"
        output = open(fileName,'wb')
        output.write(urlContent)
        output.close()
 

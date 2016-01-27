import urllib2, base64, json
from pprint import pprint
import time
import csv
from time import gmtime, strftime

now = strftime("%Y-%m-%d", gmtime())

username = 'groupmpbu_inbev_display_api@moat.com'
password = 'jUXEf2ch'

start = 20150201
end1 = 20151221
end2 = 20151231
k = 0
List = []
List.append(['date','campaign','viewability','21-34','21-49','25-54','35+'])

print "StartDisplay"
#'76349','77927','78626','78543','78781','78454','79093','78431','79750','79636','80284','79635','80652','80459','80629','80703','80736','80740','80458','80738','80968','80922','80571','80836','80965','80919',\
#'80732','80793'
campaign = ['76349','77927','78626','78543','78781','78454','79093','78431','79750','79636','80284','79635','80652','80459','80629','80703','80736','80740','80458','80738','80968','80922','80571','80836','80965','80919',\
'80732','80793','81028','81031','81635','80963']
for i in range(0,len(campaign)):
    j = end1
    while j <= end2:
        print j
        if j == 20151232:
            j = 20160101
        url = 'https://api.moat.com/1/stats.json?start='+str(start)+'&end='+str(j)+'&level1='+campaign[i]+'&level2=23177&columns=level1,level2,impressions_analyzed,in_view_percent,nielsen_age_21-34_percent,nielsen_age_21-49_percent,nielsen_age_25-54_percent,nielsen_age_35-999_percent'
        req = urllib2.Request(url)
        base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
        req.add_header("Authorization", "Basic %s" % base64string)
        try:
            result = urllib2.urlopen(req)
        except urllib2.URLError:
            print 'authorization failed'
            continue
        result_data = result.read()
        data = json.loads(result_data)
        print "middle"
        try:
            if len(data["results"]["summary"])>0 and  "nielsen_age_21-34_percent" in data["results"]["summary"].keys():
                List.append([j,data["results"]["summary"]["level1_label"],data["results"]["summary"]["in_view_percent"]/100,data["results"]["summary"]["nielsen_age_21-34_percent"]/100,
                         data["results"]["summary"]["nielsen_age_21-49_percent"]/100,data["results"]["summary"]["nielsen_age_25-54_percent"]/100,data["results"]["summary"]["nielsen_age_35-999_percent"]/100])
            print data["results"]["summary"]["level1_label"]
        except:
            j += 1
            print "slow"
            continue
        j += 1
        

print "1st"

#        pprint(data)

out_f = open('C:\\Users\\nathan.qiu\\Documents\\Moat API\\cumDisplayResult_'+now+'.csv','wb')
print "ing"
writer = csv.writer(out_f)
writer.writerows(List)
out_f.close()

print "Done"

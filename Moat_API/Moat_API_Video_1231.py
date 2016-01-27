import urllib2, base64, json
from pprint import pprint
import time
import csv
from time import gmtime, strftime

now = strftime("%Y-%m-%d", gmtime())


username = 'groupmpbu_inbev_video_api@moat.com'
password = '5udrAnus'

start = 20150201
end1 = 20151221
end2 = 20151231
k = 0
List = []
List.append(['date','campaign','AVOC','21-34','21-49','25-54','35+'])

print "StartVideo"
#'78454','79111','79093','78626','79696','80261','79635','80652','80732','80968','80703','80919','80922','81028','81031','78069','81172','81635',
campaign = ['80740']
for i in range(0,len(campaign)):
    j = end1
    while j <= end2:
        if j == 20151232:
            j = 20160101
        print j
        url = 'https://api.moat.com/1/stats.json?start='+str(start)+'&end='+str(j)+'&level1='+campaign[i]+'&level2=95553&columns=level1,level2,ad_vis_and_aud_on_complete_percent,impressions_analyzed,nielsen_age_21-34_percent,nielsen_age_21-49_percent,nielsen_age_25-54_percent,nielsen_age_35-999_percent'
        
        req = urllib2.Request(url)
        
        base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')

        req.add_header("Authorization", "Basic %s" % base64string)
        try:
            result = urllib2.urlopen(req)
        except urllib2.URLError:
            print 'authorization failed'
            continue
        try:
            result_data = result.read()
            data = json.loads(result_data)

            if len(data["results"]["summary"])>0 and  "nielsen_age_21-34_percent" in data["results"]["summary"].keys():
                List.append([j,data["results"]["summary"]["level1_label"],data["results"]["summary"]["ad_vis_and_aud_on_complete_percent"]/100,data["results"]["summary"]["nielsen_age_21-34_percent"]/100,data["results"]["summary"]["nielsen_age_21-49_percent"]/100,
                             data["results"]["summary"]["nielsen_age_25-54_percent"]/100,data["results"]["summary"]["nielsen_age_35-999_percent"]/100])
            j += 1
            print(data["results"]["summary"]["level1_label"])
        except:
            j += 1
            print "wrong"
            continue

        

out_f = open('C:\\Users\\nathan.qiu\\Documents\\Moat API\\cumVideoResult_'+now+'.csv','wb')
writer = csv.writer(out_f)
writer.writerows(List)
out_f.close()

print "Done"

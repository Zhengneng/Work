=======
# Work
Everything Related to Work
======
curl -b cookies -c cookies -X POST -d @auth.js http://api.appnexus.com/Auth | python -m json.tool


curl -b cookies -c cookies -X POST -d @domain_performance.js 'http://api.appnexus.com/report?advertiser_id=435289' |python  -m json.tool


curl -b cookies -c cookies 'http://api.appnexus.com/report?id=a61282ac52f4672d0e7eb3eb61c19e70'| python -m json.tool


curl -b cookies -c cookies 'http://api.appnexus.com/report-download?id=a61282ac52f4672d0e7eb3eb61c19e70'> /tmp/AppNexus/1025/1012-1025.csv



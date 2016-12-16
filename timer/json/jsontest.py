#config:utf-8
import json
import requests

#f = open('testjson.json','r')
f = requests.get('http://weather.livedoor.com/forecast/webservice/json/v1?city=130010').json() 

print json.dumps(f,sort_keys = True, indent = 4)

f.close()

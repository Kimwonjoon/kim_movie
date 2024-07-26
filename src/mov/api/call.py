#import requests
#import json
def req(dt="20120101"):
    base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json'
    key = '2df268e129e6b819167d9a47c41bedd0'

    url = f'{base_url}?key={key}&targetDt={dt}'

#    res = requests.get(url)
#    text = res.text
#
#    d = json.load(text)
    print(url)
req()
    

import requests
def gen_url(dt="20120101"):
    base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json'
    key = '2df268e129e6b819167d9a47c41bedd0'
    url = f'{base_url}?key={key}&targetDt={dt}'

    return url

def req(dt="20240725"):
    url = gen_url(dt)
    res = requests.get(url)
    data = res.json()
    code = res.status_code
    return code, data
print(req())

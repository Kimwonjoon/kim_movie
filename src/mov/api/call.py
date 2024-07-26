import requests
import os
def gen_url(dt="20120101"):
    base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json'
    key = get_key()
    url = f'{base_url}?key={key}&targetDt={dt}'

    return url

def req(dt="20240725"):
    url = gen_url(dt)
    res = requests.get(url)
    data = res.json()
    code = res.status_code
    return code, data

def get_key():
    key = os.getenv('MOVIE_API_KEY')
    return key

def req2dataframe():
    _, data = req()
    li = data['boxOfficeResult']['dailyBoxOfficeList']
    return li

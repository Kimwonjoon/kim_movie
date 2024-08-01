import requests
import os
import pandas as pd
def gen_url(load_dt="20120101", req_val = {}):
    base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json'
    key = get_key()
    url = f'{base_url}?key={key}&targetDt={load_dt}'
    for key, value in req_val.items():
        url = url + f'&{key}={value}'
    return url

def req(load_dt="20120101", url_param = {}):
    url = gen_url(load_dt, url_param)
    res = requests.get(url)
    data = res.json()
    code = res.status_code
    return code, data

def get_key():
    """영화진흥위원회 가입 및 API 키 생성 후 환경변수 선언 필요"""
    key = os.getenv('MOVIE_API_KEY')
    return key

def req2list(load_dt="20120101", url_param = {}) -> list:
    _, data = req(load_dt, url_param)
    li = data['boxOfficeResult']['dailyBoxOfficeList']
    return li

def list2df(load_dt="20120101", url_param = {}):
    li = req2list(load_dt, url_param)
    df = pd.DataFrame(li)
    return df

def save2df(load_dt="20120101", url_param = {}):
    df = list2df(load_dt, url_param)
    # df에 load_df 컬럼 추가 조회 일자 YYYYMMDD 형식
    # 아래 파일 저장 시 load_dt 기준으로 파티셔닝
    df['load_dt'] = load_dt
    print(df.head())
    return df

def echo(yaho):
    return yaho

def change2df(load_dt = "20120101", path = "~/tmp/test_parquet"):
    df = pd.read_parquet(f'{path}/load_dt={load_dt}')
    num_cols = ['rnum', 'rank', 'rankInten', 'salesAmt', 'audiCnt', 'audiAcc', 'scrnCnt', 'showCnt', 'salesShare', 'salesInten', 'salesChange', 'audiInten', 'audiChange']
    for c in num_cols:
        df[c] = pd.to_numeric(df[c])
    return df

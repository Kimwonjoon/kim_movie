import requests
import os
import pandas as pd
def gen_url(dt="20240725"):
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
    """영화진흥위원회 가입 및 API 키 생성 후 환경변수 선언 필요"""
    key = os.getenv('MOVIE_API_KEY')
    return key

def req2list() -> list:
    _, data = req()
    li = data['boxOfficeResult']['dailyBoxOfficeList']
    return li

def list2df():
    li = req2list()
    df = pd.DataFrame(li)
    return df

def save2df():
    df = list2df()
    # df에 load_df 컬럼 추가 조회 일자 YYYYMMDD 형식
    # 아래 파일 저장 시 load_dt 기준으로 파티셔닝
    df['load_dt'] = '20240725'
    print(df.head())
    df.to_parquet('~/tmp/test_parquet', partition_cols = ['load_dt'])
    return df

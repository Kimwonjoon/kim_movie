from mov.api.call import gen_url, req, get_key, req2list, list2df, save2df
import pandas as pd

def test_save2df():
    df = save2df()
    assert isinstance(df, pd.DataFrame)
    for i in ['rnum', 'openDt', 'movieNm', 'audiAcc']:
        assert i in df.columns

def test_list2df():
    df = list2df()
    assert isinstance(df, pd.DataFrame)
    assert 'rnum' in df.columns
    assert 'openDt' in df.columns
    assert 'movieNm' in df.columns
    assert 'audiAcc' in df.columns

def test_req2list():
    li = req2list()
    assert len(li) > 0
    assert 'rnum' in li[0].keys()
    assert li[0]['rnum'] == '1' 

def test_key():
    key = get_key()
    assert key

def test_gen_url():
    url = gen_url()
    assert True
    assert "http" in url
    assert "kobis" in url
def test_req():
    code, data = req()
    assert code == 200
    assert req("20240710")[0] == 200

    code, data = req('20230101')
    assert code == 200

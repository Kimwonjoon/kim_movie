from mov.api.call import gen_url, req, get_key, req2dataframe

def test_req2dataframe():
    li = req2dataframe()
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

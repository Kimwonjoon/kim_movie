from mov.api.call import gen_url, req

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

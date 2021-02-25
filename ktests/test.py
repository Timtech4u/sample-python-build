import requests

def test_core():
    r = requests.get('https://core.kudi.ng/ping')
    assert r.status_code == 200
    
 if __name__ == "__main__":
    test_core()

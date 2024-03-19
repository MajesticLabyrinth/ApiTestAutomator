import pytest
import pycurl
from io import BytesIO

def test_search_asteriods_with_success_pycurl():
    # Arrange:
    api_key = "DEMO_KEY"
    crl = pycurl.Curl()
    b_obj = BytesIO()
    crl.setopt(crl.URL, 'https://wiki.python.org/moin/BeginnersGuide')
    crl.setopt(crl.WRITEDATA, b_obj)
    #Act:
    crl.perform()
    crl.close()
    get_body = b_obj.getvalue()
    #Decode bytes:
    print('Output of GET request:\n%s' % get_body.decode('utf8'))
    assert len(get_body > 0)
    crl.close()

def test_target_url_response_headers():
    b_obj = BytesIO()
    crl = pycurl.Curl()
    crl.setopt(crl.URL, 'https://twitter.com')
    crl.setopt(crl.HEADERFUNCTION, display_header)
    crl.setopt(crl.WRITEDATA, b_obj)
    crl.perform()
    print('Header values:-')
    crl.close()
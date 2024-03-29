import pycurl
try:
    # Pytohn 3
    from urllib.parse import urlencode
except ImportError:
    # Python 2
    from urllib import urlencode

    c = pycurl.Curl()
    c.setopt(c.URL, 'https://httpbin.org/post')

    post_data = {'field' : 'value'}
    # Form data must be provided already urlencoded.
    postfields = urlencode(post_data)
    # Sets request method to POST,
    # Content-Type header to application/x-www-form-urlencoded
    # and data to send in request body.
    c.setopt(c.POSTFIELDS, postfields)
    # POSTFIELDS automatically sets HTTP request method to POST.
    # Other request methods can be specified via CUSTOMREQUEST option:
    # c.setopt(c.CUSTOMREQUEST, 'PATCH')

    c.perform()
    c.close()
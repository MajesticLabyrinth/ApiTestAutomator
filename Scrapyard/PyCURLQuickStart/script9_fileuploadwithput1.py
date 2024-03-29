import pycurl

c = pycurl.Curl()
c.setopt(c.URL, 'https://httpbin.org/put')

c.setopt(c.UPLOAD, 1)
file = open('body.json')
c.setopt(c.READDATA, file)

c.perform()
c.close()
# File must be kept open while CURL object is using it.
file.close()
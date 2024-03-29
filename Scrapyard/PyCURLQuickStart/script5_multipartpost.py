# To replicate behavior of file upload in an HTML form
# (specifically, a multipart form), use HTTPPOST option.
# Such an upload is performed with a POST request.
# See the next example for how to upload a file with a
# PUT request.

# If the data to be uploaded is located in a physical file, use
# FORM_FILE as shown below:

import pycurl

c = pycurl.Curl()
c.setopt(c.URL, 'https://httpbin.org/post')

c.setopt(c.HTTPPOST, [(
    'fileupload', (c.FORM_FILE, __file__,)),
])
c.perform()
c.close()
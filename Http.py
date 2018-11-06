# @author 宋疆疆 
# @since 2018/8/31.
import http
import mimetypes
import http.client
from util import Util


def post_multipart(scheme, host, port, selector, fields, files):
    """
    Post fields and files to an http host as multipart/form-data.
    fields is a sequence of (name, value) elements for regular form fields.
    files is a sequence of (name, filename, value) elements for data to be uploaded as files
    Return the server's response page.
    """
    content_type, body = encode_multipart_formdata(fields, files)
    if scheme and scheme.lower() == "http":
        h = http.client.HTTPConnection(host, port)
    else:
        h = http.client.HTTPSConnection(host, port)
    h.putrequest('POST', selector)
    h.putheader('content-type', content_type)
    h.putheader('content-length', str(len(body)))
    h.endheaders()
    h.send(body)
    return h.getresponse()


def encode_multipart_formdata(fields, files):
    """
    fields is a sequence of (name, value) elements for regular form fields.
    files is a sequence of (name, filename, value) elements for data to be uploaded as files
    Return (content_type, body) ready for httplib.HTTP instance
    """
    BOUNDARY = '----------ThIs_Is_tHe_bouNdaRY_$'
    CRLF = '\r\n'
    L = []
    body = bytes()
    for (key, value) in fields:
        L.append('--' + BOUNDARY)
        body += ('--' + BOUNDARY + CRLF).encode()
        L.append('Content-Disposition: form-data; name="%s"' % key)
        body += ('Content-Disposition: form-data; name="%s"' % key + CRLF).encode()
        L.append('')
        body += ('' + CRLF).encode()
        L.append(value)
        body += (value + CRLF).encode()
    for (key, filename, value) in files:
        L.append('--' + BOUNDARY)
        body += ('--' + BOUNDARY + CRLF).encode()
        L.append('Content-Disposition: form-data; name="%s"; filename="%s"' % (key, filename))
        body += ('Content-Disposition: form-data; name="%s"; filename="%s"' % (key, filename) + CRLF).encode()
        L.append('Content-Type: %s' % get_content_type(filename))
        body += ('Content-Type: %s' % get_content_type(filename) + CRLF).encode()
        L.append('')
        body += ('' + CRLF).encode()
        L.append(value)
        body += value + CRLF.encode()
    L.append('--' + BOUNDARY + '--')
    body += ('--' + BOUNDARY + '--' + CRLF).encode()
    L.append('')
    body += ('' + CRLF).encode()
    # body = CRLF.join(L)
    content_type = 'multipart/form-data; boundary=%s' % BOUNDARY
    # return content_type, body.encode()
    # util.cprint(body.decode())
    return content_type, body


def get_content_type(filename):
    return mimetypes.guess_type(filename)[0] or 'application/octet-stream'


def get(uri):
    if uri.scheme and uri.scheme.lower() == "http":
        h = http.client.HTTPConnection(uri.netloc, uri.port)
    else:
        h = http.client.HTTPSConnection(uri.netloc, uri.port)
    h.request('GET', uri.path)
    return h.getresponse()
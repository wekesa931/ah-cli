import urllib.request, urllib.error
import json
import click

from validators import validate
from conversions import Conversions

command = input("list / view : ")

url = 'https://ah-django-staging.herokuapp.com/api/articles'
try:
    com = validate(command)
    conn = urllib.request.urlopen(url+"{}".format(com[0]))
    the_page = conn.read().decode('utf8')
    response_code = conn.getcode()
    if com[1] != None:
        data = json.loads(the_page)[com[1]]
        article_res = json.dumps(data, indent=4, sort_keys=True)
        Conversions.writeToJson('./', 'articles', article_res)
        Conversions.converToCsv('./', 'articles', article_res)
    else:
        data = json.loads(the_page)
        res = json.dumps(data, indent=4, sort_keys=True)
        Conversions.writeToJson('./', 'articles', res)
except urllib.error.HTTPError as e:
    # Return code error (e.g. 404, 501, ...)
    # ...
    print('HTTPError: {}'.format(e.code))
except urllib.error.URLError as e:
    # Not an HTTP-specific error (e.g. connection refused)
    # ...
    print('URLError: {}'.format(e.reason))



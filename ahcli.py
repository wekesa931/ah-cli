import urllib.request, urllib.error
import json
import click

from validators import validate
from conversions import Conversions

# command = input("list / view : ")

url = 'https://ah-django-staging.herokuapp.com/api/articles'
# try:
#     com = validate(command)
#     conn = urllib.request.urlopen(url+"{}".format(com[0]))
#     the_page = conn.read().decode('utf8')
#     response_code = conn.getcode()
#     if com[1] != None:
#         data = json.loads(the_page)[com[1]]
#         article_res = json.dumps(data, indent=4, sort_keys=True)
#         Conversions.writeToJson('./', 'articles', article_res)
#         Conversions.converToCsv('./', 'articles', article_res)
#     else:
#         data = json.loads(the_page)
#         res = json.dumps(data, indent=4, sort_keys=True)
#         Conversions.writeToJson('./', 'articles', res)
# except urllib.error.HTTPError as e:
#     # Return code error (e.g. 404, 501, ...)
#     # ...
#     print('HTTPError: {}'.format(e.code))
# except urllib.error.URLError as e:
#     # Not an HTTP-specific error (e.g. connection refused)
#     # ...
#     print('URLError: {}'.format(e.reason))

# @click.group()
# def cli():
#     pass

# @click.command()
# def list():
#     conn = urllib.request.urlopen(url+"/feed/")
#     the_page = conn.read().decode('utf8')
#     response_code = conn.getcode()
#     data = json.loads(the_page)['results']
#     print(data)
#     article_res = json.dumps(data, indent=4, sort_keys=True)
#     Conversions.writeToJson('./', 'articles', article_res)
#     Conversions.converToCsv('./', 'articles', article_res)

@click.group()
def cli():
    pass

@cli.command()
@click.option('--slug', default="feed",
                help='A string to show emotions')
def list(slug):
    try:
        new_url =url + '/' + slug + '/'
        conn = urllib.request.urlopen(new_url)
        the_page = conn.read().decode('utf8')
        response_code = conn.getcode()
        if slug == 'feed':
            data = json.loads(the_page)['results']
            article_res = json.dumps(data, indent=4, sort_keys=True)
            Conversions.writeToJson('./', 'articles', article_res)
            Conversions.converToCsv('./', 'articles', article_res)
            print(article_res)
        else:
            data = json.loads(the_page)
            res = json.dumps(data, indent=4, sort_keys=True)
            Conversions.writeToJson('./', 'articles', res)
            print(res)
    except urllib.error.HTTPError as e:
        # Return code error (e.g. 404, 501, ...)
        # ...
        error = json.dumps({'message': 'Not Found!',
                 'HTTPError': e.code}, indent=4, sort_keys=True)
        print(error)
    except urllib.error.URLError as e:
        # Not an HTTP-specific error (e.g. connection refused)
        # ...
        print('URLError: {}'.format(e.reason))

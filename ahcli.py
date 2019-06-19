import urllib.request, urllib.error
import json
import click

from validators import validate
from conversions import Conversions

url = 'https://ah-django-staging.herokuapp.com/api/articles'

@click.group()
def cli():
    pass

@cli.command()
@click.option('--slug', default="feed",
                help='A string to show emotions')
@click.option('--limit', default=None,
                help='A string to show emotions')
def list(slug,limit):
    try:
        new_url =url + '/' + slug + '/'
        conn = urllib.request.urlopen(new_url)
        the_page = conn.read().decode('utf8')
        response_code = conn.getcode()
        print(response_code)
        new_data = None
        if slug == 'feed':
            data = json.loads(the_page)['results']
            if limit:
                new_data = (data[0:int(limit)])
                data = new_data
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


@cli.command()
@click.option('--by', default='',
                help='A string to show emotions')
def search(by):
    prefix = '/search?'
    try:
        new_url =url + prefix + by
        conn = urllib.request.urlopen(new_url)
        the_page = conn.read().decode('utf8')
        response_code = conn.getcode()
        res = json.loads(the_page)
        data = json.dumps(res, indent=4, sort_keys=True)
        print(data)
    except urllib.error.HTTPError as e:
        # Return code error (e.g. 404, 501, ...)
        # ...
        error = json.dumps({'message': 'Not Found!',
                 'HTTPError': e.code}, indent=4, sort_keys=True)
        print(error)

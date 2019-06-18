import urllib.request, urllib.error
import json
import csv
from validators import validate

def converToCsv(path, fileName, data):
    file = './' + path + '/' + fileName + '.csv'
    with open(file, 'w') as articles:
        print(type(data))
        data = json.loads(data)
        column_items = data[0]
        fieldNames = []
        for key, value in column_items.items():
            fieldNames.append(key)
        theWriter = csv.DictWriter(articles, fieldnames=fieldNames)

        theWriter.writeheader()
        
        all_items = {}
        for article in data:
            for key, value in article.items():
                all_items.update({key: value})
            theWriter.writerow(all_items)

def writeToJson(path, fileName, data):
    file = './' + path + '/' + fileName + '.json'
    with open(file, 'w') as articles:
        data = json.loads(data)
        json.dump(data, articles, indent=4, sort_keys=True)

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
        writeToJson('./', 'articles', article_res)
    else:
        data = json.loads(the_page)
        res = json.dumps(data, indent=4, sort_keys=True)
        writeToJson('./', 'articles', res)
        converToCsv('./', 'articles', res)
except urllib.error.HTTPError as e:
    # Return code error (e.g. 404, 501, ...)
    # ...
    print('HTTPError: {}'.format(e.code))
except urllib.error.URLError as e:
    # Not an HTTP-specific error (e.g. connection refused)
    # ...
    print('URLError: {}'.format(e.reason))



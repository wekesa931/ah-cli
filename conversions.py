import json
import csv


class Conversions():

    def converToCsv(path, fileName, data):
        file = './' + path + '/' + fileName + '.csv'
        with open(file, 'w') as articles:
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
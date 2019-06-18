def validate(command):
    if command == 'list':
        url_extension = '/feed/'
        results = 'results'
        return [url_extension, results]
    elif command == 'view':
        slug = input("Input slug : ")
        url_slug = '/' + slug + '/'
        return [url_slug, None]
    else:
        pass

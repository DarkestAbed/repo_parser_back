def parse_url_with_amperson(url: str):
    # execution
    # # check if '&' char is on url
    is_amperson_on_url = url.find("&")
    # # if no amperson, return url
    if is_amperson_on_url == -1:
        return None
    elif is_amperson_on_url > 0:
        url_return = url.replace("&sol", "/")
        return url_return
    else:
        raise Exception("Error parsing string")


def parse_url_with_quotes(url: str):
    # execution
    # # check if '&' char is on url
    is_quotes_on_url = url.find('"')
    # # if no amperson, return url
    if is_quotes_on_url == -1:
        return None
    elif is_quotes_on_url > 0:
        url_return = url.replace('"', "")
        return url_return
    else:
        raise Exception("Error parsing string")


def parse_url(url: str):
    try_amperson = parse_url_with_amperson(url=url)
    if not try_amperson is None:
        return try_amperson
    try_quotes = parse_url_with_quotes(url=url)
    if not try_quotes is None:
        return try_quotes

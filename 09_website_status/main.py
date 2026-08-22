# %%
import requests
from requests import Response
from typing import Any


# 1. Create a helper function that always makes sure the url is formatted properly
def normalise_url(url: str) -> str:
    return url if url.startswith(('http://', 'https://')) else f'https://{url}'


# 2. Check the website
def check_website(url: str, timeout: int = 10) -> Response | None:
    url = normalise_url(url)

    print(f'\n=== Website diagnostics for {url} ===')
    try:
        response: Response = requests.get(url, timeout=timeout)
        return response
    except Exception as e:
        print(f'ERROR: {e}')
        return


# 3. Organise and display the data
def display_data(response):
    try:
        status_code: int = response.status_code
        elapsed_time: float = response.elapsed.total_seconds()
        reason: str = response.reason
        content_type: str = response.headers.get('Content-Type', '')
        encoding: str | None = response.encoding
        headers: dict[str, str] = dict(response.headers)

        print(f'Status code  : {status_code} ({reason})')
        print(f'Elapsed time : {elapsed_time}s')
        print(f'Content-Type : {content_type}')
        print(f'Encoding     : {encoding or 'n/a'}')
        print('Headers      :')
        for key, value in headers.items():
            print(f'  • {key}: {value}')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    display_data(check_website('www.asdfefaapple.com'))

# Homework:
# 1. Split "check_website()" into two functions. Make it so that "check_website()" returns
# data that you can then insert into another function called "display_website(data)" to see the
# information in the console.

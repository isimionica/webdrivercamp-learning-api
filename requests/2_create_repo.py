import requests
from pprint import pprint


def create_repo(url):
    header = {'Authorization': 'token'}
    payload = {
        'name': 'repo-created-with-api',
        'private': True,
        'has_wiki': False
    }

    response = requests.post(url, headers=header, json=payload)
    print(f'Response status code: {response.status_code}')

    return response.json()

if __name__ == '__main__':
    url = 'https://api.github.com/user/repos'

    repo = create_repo(url)
    pprint(repo)
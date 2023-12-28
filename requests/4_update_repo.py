import requests

def update_repo(url):
    header = {'Authorization': 'token'}
    payload = {'description': 'I know Python Requests!'}

    response = requests.patch(url, headers=header, json=payload)

    print(f'Response status code: {response.status_code}')
    repo = response.json()

    return repo

if __name__=='__main__':
    url = 'https://api.github.com/repos/arturadamian/repo-created-with-api'
    owner = "isimionica"
    repo = "repo-created-with-api"

    repo = update_repo(url)
    assert repo['description'] == 'I know Python Requests!'
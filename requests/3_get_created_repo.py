import requests

def get_created_repo(url):
    header = {'Authorization': 'token'}
    response = requests.get(url, headers = header)

    print(f'Response status code: {response.status_code}')
    repo = response.json()
    assert repo['has_wiki'] == False
    assert repo['private'] == True
    assert repo['name'] == 'repo-created-with-api'
    assert repo['owner']['login'] == 'isimionica'

if __name__=="__main__":
    url = "https://api.github.com/repos/{owner}/{repo}"
    owner = "isimionica"
    repo = "repo-created-with-api"

    get_created_repo(url)
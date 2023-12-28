import requests

def delete_repo(url):
    header= {'Authorization': 'token'}

    response = requests.delete(url, headers=header)

    print(f'Response status code: {response.status_code}')


if __name__=="__main__":
    url = f'https://api.github.com/repos/{owner}/{repo}'
    owner = "isimionica"
    repo = "repo-created-with-api"

    delete_repo(url)
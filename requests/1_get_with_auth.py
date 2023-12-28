import requests


def get_with_auth(url):
    header = {'Authorization': 'token'}
    response = requests.get(url, headers = header)
    print(f'Response status code: {response.status_code}')

    return len(response.json()), response.headers




if __name__ == "__main__":
    url = "https://api.github.com/user/repos"

    num_of_repos, headers = get_with_auth(url)

    print(f"Total Repos: {num_of_repos}")
    print(f"Response headers: {headers}")
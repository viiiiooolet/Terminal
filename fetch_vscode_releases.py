import requests

def get_info(url):
    headers = {}
    results = []
    page = 1
    per_page = 100  # GitHub API 最多每页 100 个结果

    while True:
        params = {'page': page, 'per_page': per_page}
        response = requests.get(url, headers=headers, params=params)
        if response.status_code != 200:
            print(f'Error: {response.status_code} - {response.text}')
            break
        data = response.json()
        if not data:
            break
        results.extend(data)
        page += 1

    return results

def fetch_vscode_releases(owner='microsoft', repo='vscode'):
    url = f'https://api.github.com/repos/{owner}/{repo}/releases'
    releases = get_info(url)
    return releases